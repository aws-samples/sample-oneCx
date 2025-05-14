import boto3
import csv
import json
import os
from io import StringIO
import psycopg2
from psycopg2 import sql
from botocore.exceptions import ClientError
import logging
import random
from datetime import datetime, timedelta

logger = logging.getLogger()
logger.setLevel(logging.INFO)

function_arn = os.environ.get('FUNCTION_ARN')
if not function_arn:  
    raise ValueError("FUNCTION_ARN environment variable is not set")

def get_secret():
    logger.info("Retrieving secret from Secrets Manager")
    secret_arn = os.environ['DB_SECRET_ARN']
    region_name = os.environ['AWS_REGION']

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_arn)
        logger.info("Secret retrieved successfully")
        return json.loads(get_secret_value_response['SecretString'])
    except ClientError as e:
        logger.error(f"Error retrieving secret: {str(e)}")
        raise

def create_trigger(conn):
    with conn.cursor() as cur:
        # First, ensure the aws_lambda extension is installed
        cur.execute("CREATE EXTENSION IF NOT EXISTS aws_lambda CASCADE;")

        # Create or replace the invoke_promptflow_lambda function
        cur.execute("""
            CREATE OR REPLACE FUNCTION invoke_promptflow_lambda(input_payload JSON, lambda_arn TEXT)
            RETURNS TABLE(status_code INTEGER, response_payload JSON, executed_version TEXT, log_result TEXT) AS $$
            BEGIN
              RETURN QUERY SELECT 
                (result).status_code,
                (result).payload,
                (result).executed_version,
                (result).log_result
              FROM (
                SELECT aws_lambda.invoke(
                  aws_commons.create_lambda_function_arn(lambda_arn),
                  input_payload,
                  'RequestResponse'
                ) AS result
              ) subquery;
            END;
            $$ LANGUAGE plpgsql;
        """)

        # Create or replace the notify_insert function using parameterized query
        cur.execute("""
            CREATE OR REPLACE FUNCTION notify_insert()
            RETURNS TRIGGER AS $$
            DECLARE
                lambda_result RECORD;
                lambda_arn TEXT := %s;
            BEGIN
                SELECT * FROM invoke_promptflow_lambda(
                    json_build_object(
                        'table', TG_TABLE_NAME,
                        'action', TG_OP,
                        'event_id', NEW.event_id,
                        'customer_id', NEW.customer_id,
                        'event_type_id', NEW.event_type_id,
                        'event_description', NEW.event_description,
                        'timestamp', NEW.timestamp
                    ),
                    lambda_arn
                ) INTO lambda_result;

                PERFORM pg_notify('insert_channel', json_build_object(
                    'table', TG_TABLE_NAME,
                    'action', TG_OP,
                    'event_id', NEW.event_id,
                    'customer_id', NEW.customer_id,
                    'event_type_id', NEW.event_type_id,
                    'event_description', NEW.event_description,
                    'timestamp', NEW.timestamp
                )::text);

                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;
        """, [function_arn])

        # Create the trigger
        cur.execute("""
            DROP TRIGGER IF EXISTS customer_journey_insert_trigger ON customer_journeys;
            CREATE TRIGGER customer_journey_insert_trigger
            AFTER INSERT ON customer_journeys
            FOR EACH ROW
            EXECUTE FUNCTION notify_insert();
        """)

        # Create the trigger
        cur.execute("""
            DROP TRIGGER IF EXISTS customer_journey_insert_trigger ON customer_journeys;
            CREATE TRIGGER customer_journey_insert_trigger
            AFTER INSERT ON customer_journeys
            FOR EACH ROW
            EXECUTE FUNCTION notify_insert();
        """)

    conn.commit()
    logger.info("Trigger, functions, and necessary columns created successfully")

def handler(event, context):
    logger.info("Lambda function started")

    try:
        secret = get_secret()

        with psycopg2.connect(
                host=secret['host'],
                user=secret['username'],
                password=secret['password'],
                dbname='postgres'
        ) as conn:
            create_trigger(conn)

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise