import json
import os
import boto3
from botocore.exceptions import ClientError
import logging
import urllib.request
import urllib.parse
from dateutil import parser
from datetime import datetime, date

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def parse_date(date_string):
    try:
        # Try to parse the date string using the dateutil.parser
        return parser.parse(date_string).date()
    except ValueError as e:
        # If parsing fails, log the error and return the original string
        logger.warning(f"Failed to parse date '{date_string}': {str(e)}")
        return date_string

def lambda_handler(event, context):
    try:
        print('event:', json.dumps(event))
        query_params = event['queryStringParameters']
        logger.info(f"Query parameters: {query_params}")
        customer_id = query_params.get('customer_id')
        start_date_str = query_params.get('start_date')
        end_date_str = query_params.get('end_date')
        num_days = query_params.get('num_days')
        #insight_prompt = query_params.get('insight_prompt')

        if not customer_id:
            logger.error('Missing required parameter: customer_id')
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'customer_id is required'}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                },
            }

        # Parse and validate the start and end dates
        start_date = parse_date(start_date_str) if start_date_str else None
        end_date = parse_date(end_date_str) if end_date_str else None

        if start_date and end_date and start_date > end_date:
            logger.error('Start date cannot be greater than end date.')
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Start date cannot be greater than end date'}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                },
            }

        params = {
            'customer_id': customer_id
        }

        if start_date:
            params['start_date'] = start_date.strftime('%Y-%m-%d')
        if end_date:
            params['end_date'] = end_date.strftime('%Y-%m-%d')

        # Construct the full URL with parameters
        url = f"{os.environ['API_ENDPOINT']}?{urllib.parse.urlencode(params)}"

        request = urllib.request.Request(url)
        api_key_id = os.environ['GET_CUSTOMER_JOURNEY_API_KEY']
       
        # Get API key value from API GW using the API KEY ID
        client = boto3.client('apigateway')
        api_key_value = client.get_api_key(apiKey=api_key_id, includeValue=True)['value']
        print('api_key_value:', api_key_value)
        request.add_header('x-api-key', api_key_value)

        with urllib.request.urlopen(request) as response:
            # Read the response content as string first
            response_content = response.read().decode('utf-8')
            # Then parse it as JSON
            try:
                data = json.loads(response_content)
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON response: {response_content}")
                logger.error(f"JSON decode error: {str(e)}")
                return {
                    'statusCode': 500,
                    'body': json.dumps({'error': 'Invalid JSON response from API'}),
                    'headers': {
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    },
                }

        logger.info(f"Response data: {data}")
           

        # Use Amazon Bedrock Messages API with Anthropic Claude 3 Haiku model to summarize the customer journey data.
        bedrock = boto3.client("bedrock-runtime")
        prompt_message = '''
        You are an expert in analyzing customer journeys for Telco operator. Summarize the customer journey data
        only based on the data provide inside the <input> </input> tag. The summry should be based on the patterns,
        behaviors, and notable similarities or differences. Skip the preamble and generate only the summary text for business
        executives to make customer experience decision. The summary should be short and not more than 200 words.

        If there is a number of days value available in the 'Duration' field then use the 'CustomerJourneyEvents'
        only for that particular duration. For example, if the duration is 30 then use only the 'CustomerJourneyEvents'
        occured in the last 30 days for the summary.
        
        <input>
            "CustomerId": {id}
            "CustomerJourneyEvents": {data}
            "Duration": {duration}
        </input>
        '''.format(id =customer_id, data=json.dumps(data), duration=num_days)

        body = json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 500,
                "temperature": 0,
                "top_p": 1,
                "top_k": 50,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt_message
                            }
                        ]
                    }
                ]
            }
        )
        modelId = 'anthropic.claude-3-haiku-20240307-v1:0'
        accept = 'application/json'
        contentType = 'application/json'
        response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
        
        response_data = json.loads(response["body"].read())
        if not response_data:
            logger.error("No response data from Bedrock.")
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Error generating summary."}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                },
            }
        if "content" in response_data:
            summary = response_data["content"]
            summarized_data = {
                "customer_id": customer_id,
                "summary": summary
            }
            return {
                "statusCode": 200,
                "body": json.dumps(summarized_data),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                },
            } 
        else:
            logger.info("Missing 'content' key in Bedrock response.")
            return {
                "statusCode": 200,
                "body": json.dumps({"Response": json.dumps(response_data)}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                },
            }
    except KeyError as e:
        logger.error(f"Missing required parameter: {str(e)}")
    except urllib.error.URLError as e:
        logger.error(f"URL Error: {str(e)}")
        raise
    except ClientError as e:
        logger.error(f"AWS SDK Exception: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Exception: {str(e)}")
        raise