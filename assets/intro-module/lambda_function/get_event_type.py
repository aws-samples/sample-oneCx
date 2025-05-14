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
        query_params = event.get('queryStringParameters', {})
        logger.info(f"Query parameters: {query_params}")
        event_type_id = query_params.get('event_type_id')
        event_type_name = query_params.get('event_type_name')
        
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

        with conn.cursor() as cur:
            if event_type_id:
                query = """
                    SELECT
                        event_type_name,
                        event_type_description
                    FROM event_type
                    WHERE event_type_id = %s
                """
                params = [event_type_id]
            elif event_type_name:
                query = """
                    SELECT
                        event_type_id,
                        event_type_description
                    FROM event_type
                    WHERE event_type_name = %s
                """
                params = [event_type_name]
            else:
                query = """
                    SELECT
                        event_type_id,
                        event_type_name,
                        event_type_description
                    FROM event_type
                """
                params = []

            cur.execute(query, params)
            logger.info("Query executed successfully")

            # Construct the response JSON
            data = {
                'event_types': []
            }

            for row in cur:
                if event_type_id:
                    event_data = {
                        'event_type_id': event_type_id,
                        'event_type_name': row[0],
                        'event_type_description': row[1]
                    }
                elif event_type_name:
                    event_data = {
                        'event_type_id': row[0],
                        'event_type_name': event_type_name,
                        'event_type_description': row[1]
                    }
                else:
                    event_data = {
                        'event_type_id': row[0],
                        'event_type_name': row[1],
                        'event_type_description': row[2]
                    }
                data['event_types'].append(event_data)

        conn.close()

        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }

    except Exception as e:
        logger.error(f'Error in lambda_handler: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'An error occurred while processing the request'})
        }
