import boto3
import json
import os
import psycopg2
from psycopg2 import sql
from botocore.exceptions import ClientError
import logging
from datetime import datetime, date, timedelta

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_secret():
    """Retrieve database credentials from AWS Secrets Manager"""
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


def get_min_max_timestamps(conn):
    """Get the minimum and maximum timestamps from the database"""
    query = "SELECT MIN(timestamp), MAX(timestamp) FROM customer_journeys"

    with conn.cursor() as cur:
        cur.execute(query)
        min_timestamp, max_timestamp = cur.fetchone()

    # Convert timestamps to offset-naive datetime objects
    if isinstance(min_timestamp, datetime):
        min_timestamp = min_timestamp.replace(tzinfo=None)
    if isinstance(max_timestamp, datetime):
        max_timestamp = max_timestamp.replace(tzinfo=None)

    # If they're strings, parse them as offset-naive
    if isinstance(min_timestamp, str):
        min_timestamp = datetime.strptime(min_timestamp, "%Y-%m-%d %H:%M:%S")
    if isinstance(max_timestamp, str):
        max_timestamp = datetime.strptime(max_timestamp, "%Y-%m-%d %H:%M:%S")

    return min_timestamp, max_timestamp


def handler(event, context):
    """Main Lambda handler function"""
    conn = None
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        query_params = event.get("queryStringParameters", {})
        logger.info(f"Query parameters: {query_params}")

        # Extract query parameters
        customer_id = query_params.get("customer_id")
        start_date_str = query_params.get("start_date")
        end_date_str = query_params.get("end_date")
        num_days_str = query_params.get("num_days")

        if not customer_id:
            logger.error("Missing required parameter: customer_id")
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "customer_id is required"}),
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                },
            }

        # Retrieve database credentials from AWS Secrets Manager
        secret = get_secret()
        db_host = secret["host"]
        db_name = secret["dbname"]
        db_user = secret["username"]
        db_password = secret["password"]
        db_port = secret["port"]

        logger.info(
            f"Attempting to connect to database: host={db_host}, database={db_name}, user={db_user}, port={db_port}"
        )

        # Connect to the PostgreSQL database
        try:
            conn = psycopg2.connect(
                host=db_host,
                database=db_name,
                user=db_user,
                password=db_password,
                port=db_port,
                connect_timeout=10,
            )
            conn.set_session(autocommit=True)
            logger.info("Successfully connected to the database")
        except psycopg2.Error as e:
            logger.error(f"Error connecting to the database: {e}")
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Database connection error"}),
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                },
            }

        # Parse and validate dates if provided
        start_datetime = None
        end_datetime = None

        if num_days_str:
            try:
                num_days = int(num_days_str)
                if num_days <= 0:
                    raise ValueError("num_days must be a positive integer")
                
                # Get the latest event date from the database
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT MAX(timestamp)
                        FROM customer_journeys
                        WHERE customer_id = %s
                    """, (customer_id,))
                    latest_date = cur.fetchone()[0]

                if latest_date:
                    end_datetime = latest_date.replace(hour=23, minute=59, second=59)
                    start_datetime = (end_datetime - timedelta(days=num_days-1)).replace(hour=0, minute=0, second=0)
                else:
                    logger.warning(f"No events found for customer_id: {customer_id}")
                    return {
                        "statusCode": 200,
                        "body": json.dumps({"customer_id": customer_id, "events": []}),
                        "headers": {
                            "Access-Control-Allow-Origin": "*",
                            "Access-Control-Allow-Headers": "Content-Type",
                            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                        },
                    }
            except ValueError as e:
                logger.error(f"Invalid num_days parameter: {str(e)}")
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "num_days must be a positive integer"}),
                    "headers": {
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Headers": "Content-Type",
                        "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                    },
                }
        elif start_date_str and end_date_str:
            try:
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

                if start_date > end_date:
                    logger.error("Start date cannot be greater than end date.")
                    return {
                        "statusCode": 400,
                        "body": json.dumps({"error": "Start date cannot be greater than end date"}),
                        "headers": {
                            "Access-Control-Allow-Origin": "*",
                            "Access-Control-Allow-Headers": "Content-Type",
                            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                        },
                    }

                # Format dates for SQL query
                start_datetime = start_date.replace(hour=0, minute=0, second=0)
                end_datetime = end_date.replace(hour=23, minute=59, second=59)

            except ValueError as e:
                logger.error(f"Invalid date format: {str(e)}")
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "Date format should be YYYY-MM-DD"}),
                    "headers": {
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Headers": "Content-Type",
                        "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                    },
                }

        # Execute database query
        with conn.cursor() as cur:
            if start_datetime and end_datetime:
                query = """
                    SELECT
                        event_id,
                        event_type_id,
                        event_description,
                        timestamp
                    FROM customer_journeys
                    WHERE customer_id = %s
                    AND timestamp BETWEEN %s AND %s
                    ORDER BY timestamp
                """
                cur.execute(query, (customer_id, start_datetime, end_datetime))
            else:
                query = """
                    SELECT
                        event_id,
                        event_type_id,
                        event_description,
                        timestamp
                    FROM customer_journeys
                    WHERE customer_id = %s
                    ORDER BY timestamp
                """
                cur.execute(query, (customer_id,))

            # Construct the response JSON
            data = {"customer_id": customer_id, "events": []}

            for row in cur:
                event_timestamp = row[3]
                formatted_date = event_timestamp.strftime("%Y-%m-%d %H:%M:%S") if isinstance(event_timestamp, datetime) else str(event_timestamp)

                event_data = {
                    "event_id": row[0],
                    "event_type_id": row[1],
                    "event_description": row[2],
                    "timestamp": formatted_date,
                }
                data["events"].append(event_data)

        return {
            "statusCode": 200,
            "body": json.dumps(data),
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
            },
        }

    except Exception as e:
        logger.error(f"Error in lambda_handler: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "An error occurred while processing the request"}),
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
            },
        }
    finally:
        if conn:
            conn.close()
            logger.info("Database connection closed")
