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
        customer_id = input_data.get('customer_id')
        event_id = input_data.get('event_id')
        event_type_id = input_data.get('event_type_id')
        event_description = input_data.get('event_description')
        timestamp = input_data.get('timestamp')

    except (KeyError, json.JSONDecodeError):
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid input JSON')
        }
    
    # Check if the mandatory parameter event_type_id is present
    mandatory_params = ['event_type_id', 'customer_id', 'event_id', 'event_description', 'timestamp']
    missing_params = [param for param in mandatory_params if param not in input_data]

    if missing_params:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Missing mandatory parameter(s): {", ".join(missing_params)}')
        }
    
    # Check if event_type_id is there in the event_type table
    secret = get_secret()
    db_host = secret['host']
    db_name = 'postgres'
    db_user = secret['username']
    db_password = secret['password']
    db_port = secret['port']

    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password,
        port=db_port
    )

    cur = conn.cursor()
    query = sql.SQL("SELECT event_type_id FROM event_type WHERE event_type_id = %s")
    cur.execute(query, (event_type_id,))
    result = cur.fetchone()

    if not result:
        return {
            'statusCode': 400,
            'body': json.dumps('Event type not registered, Invalid event_type_id')
        }

    # Insert the data into the customer_journey table
    cur = conn.cursor()
    query = sql.SQL("INSERT INTO customer_journeys (customer_id, event_id, event_type_id, event_description, timestamp) VALUES (%s, %s, %s, %s, %s)")
    cur.execute(query, (customer_id, event_id, event_type_id, event_description, timestamp))
    conn.commit()

    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted successfully')
    }
    

