import boto3
import json
import os
import psycopg2
from psycopg2 import sql
from botocore.exceptions import ClientError
import logging
from datetime import datetime, date

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

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

def handler(event, context):
    try:
        logger.info(f'Received event: {json.dumps(event)}')
        input_data = json.loads(event.get('body', {}))
        logger.info(f"Query parameters: {input_data}")
        event_type_id = input_data.get('event_type_id')
        event_type_name = input_data.get('event_type_name')
        event_type_description = input_data.get('event_type_description')
    except (KeyError, json.JSONDecodeError):
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid input JSON')
        }
    
    # Check if the mandatory parameter event_type_id is present
    if 'event_type_id' not in input_data:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing mandatory parameter: event_type_id')
        }

    # Retrieve database credentials from AWS Secrets Manager
    secret = get_secret()
    db_host = secret['host']
    db_name = 'postgres'
    db_user = secret['username']
    db_password = secret['password']
    db_port = secret['port']
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password,
        port=db_port
    )

    try:
        # Connect to the database
        cur = conn.cursor()

        # Check if the event_type_id already exists
        cur.execute("SELECT EXISTS(SELECT 1 FROM event_type WHERE event_type_id = %s)", (event_type_id,))
        exists = cur.fetchone()[0]

        if exists:
            conn.close()
            return {
                'statusCode': 409,
                'body': json.dumps(f'Event type with ID {event_type_id} already exists')
            }

        # Insert the new event type
        insert_query = sql.SQL("""
            INSERT INTO event_type (event_type_id, event_type_name, event_type_description)
            VALUES (%s, %s, %s)
        """)
        cur.execute(insert_query, (event_type_id, event_type_name, event_type_description))

        conn.commit()
        conn.close()

        return {
            'statusCode': 201,
            'body': json.dumps(f'Event type with ID {event_type_id} successfully inserted')
        }

    except psycopg2.Error as e:
        if conn:
            conn.close()
        return {
            'statusCode': 500,
            'body': json.dumps(f'Database error: {str(e)}')
        }

    except Exception as e:
        if conn:
            conn.close()
        return {
            'statusCode': 500,
            'body': json.dumps(f'An error occurred: {str(e)}')
        }

