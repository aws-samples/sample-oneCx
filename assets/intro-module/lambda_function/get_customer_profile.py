import boto3
import json
import os
import psycopg2
from psycopg2 import sql
from botocore.exceptions import ClientError
import logging
from datetime import datetime, date
from decimal import Decimal

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Custom JSON Encoder to handle Decimal types
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)


def get_secret():
    logger.info("Retrieving secret from Secrets Manager")
    secret_arn = os.environ["DB_SECRET_ARN"]
    region_name = os.environ["AWS_REGION"]

    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_arn)
        logger.info("Secret retrieved successfully")
        return json.loads(get_secret_value_response["SecretString"])
    except ClientError as e:
        logger.error(f"Error retrieving secret: {str(e)}")
        raise


def handler(event, context):
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        query_params = event.get("queryStringParameters", {})
        logger.info(f"Query parameters: {query_params}")
        customer_id = query_params.get("customer_id")

        # Retrieve database credentials from AWS Secrets Manager
        secret = get_secret()
        db_host = secret["host"]
        db_name = "postgres"
        db_user = secret["username"]
        db_password = secret["password"]
        db_port = secret["port"]

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port,
        )

        if not customer_id:
            logger.error("Missing required parameter: customer_id")
            return {
                "statusCode": 400,
                "body": json.dumps(
                    {"error": "customer_id is required"}, cls=DecimalEncoder
                ),
            }

        with conn.cursor() as cur:
            # Fetch events from the PostgreSQL database using customer_id
            query = """
                SELECT
                    address,
                    contact_number,
                    email,
                    persona,
                    current_plan,
                    monthly_bill,
                    churn_propensity,
                    contract_period,
                    ltv,
                    tenure,
                    time_remaining,
                    regional_competitor_pricing
                FROM customer_profile
                WHERE customer_id = %s
            """
            params = [customer_id]

            cur.execute(query, params)
            logger.info("Query executed successfully")

            # Construct the response JSON
            data = {"customer_id": customer_id, "events": []}

            for row in cur:
                event_data = {
                    "address": row[0],
                    "contact_number": row[1],
                    "email": row[2],
                    "persona": row[3],
                    "current_plan": row[4],
                    "monthly_bill": row[5],
                    "churn_propensity": row[6],
                    "contract_period": row[7],
                    "ltv": row[8],
                    "tenure": row[9],
                    "time_remaining": row[10],
                    "regional_competitor_pricing": row[11],
                }
                data["events"].append(event_data)

        conn.close()

        return {
            "statusCode": 200,
            "body": json.dumps(data, cls=DecimalEncoder),
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                "Content-Type": "application/json",
            },
        }

    except Exception as e:
        logger.error(f"Error in lambda_handler: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps(
                {"error": "An error occurred while processing the request"}
            ),
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                "Content-Type": "application/json",
            },
        }
