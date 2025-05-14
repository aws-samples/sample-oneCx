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

def handler(event, context):
    try:
        print('event:', json.dumps(event))
        body = json.loads(event['body'])
        logger.info(f"Request body: {body}")

        customer_id = body.get('customer_id')
        num_days = body.get('num_days')
        question = body.get('prompt')
        chat_history = body.get('chat_history')


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

        params = {
            'customer_id': customer_id,
            'num_days': num_days
        }

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
            # Parse the JSON response
            data = json.load(response)

        logger.info(f"Response data: {data}")

        # Use Amazon Bedrock Messages API with Anthropic Claude 3 Sonnet model to summarize the customer journey data.
        bedrock = boto3.client("bedrock-runtime")
        prompt_message = '''You are a Telco customer journey analyst. Analyze ONLY the data within <input></input> tags to answer the question in InsightPrompt.

        Key Instructions:
        - For the Duration of {duration} days:
          * Only analyze events from latest date backwards for {duration} days
          * Example: If latest event is 2024-05-21 and duration is 7 days, analyze events from 2024-05-21 to 2024-05-15
          * STRICTLY analyze events between [latest_date - duration] to [latest_date] only
          * Do NOT make assumptions about data outside this range
          * ALWAYS start from the latest event date in the data
          * If uncertain about any data point, state "Information not available"

        - Event Filtering:
          * Before analysis, filter out all events that fall outside the calculated date range
          * Only count and analyze events that occur within the specified date range
          * Disregard any events or information from dates earlier than the start of the specified range

        - Data Usage Analysis Guidelines:
          * Only count events that have complete information
          * If asked to list specific issues/events, only include those explicitly present in the data
          * Verify count matches actual data before responding
          * When asked about data usage, only include:
            - Total browsing data (sum of all browsing_data_used)
            - Total streaming data (sum of all video_streaming_data_used)
          * Do NOT include voice_minutes in data usage calculations
          * Traditional voice calls (voice_minutes_used) should only be mentioned if specifically asked about voice usage
          * Round all data totals to 1 decimal place
          * Aggregate similar data types unless individual breakdown is requested

        - IMPORTANT:
          * Ignore previous context unless specifically relevant to current data
          * Do NOT extrapolate or infer information not present in data
          * If data appears inconsistent, report only what is verifiable
          * If no duration specified, analyze all events
          * Keep response under 200 words

        - Format output in a single line: Duration: [latest_date - duration] to  [latest_date] Answer: [specific response to InsightPrompt]

        <input>
        "CustomerId": {id}
        "CustomerJourneyEvents": {data}
        "Duration": {duration} days
        "InsightPrompt": {question}
        "PromptHistory": {history}
        </input>
        '''.format(
            id=customer_id, 
            data=json.dumps(data), 
            duration=num_days, 
            question=question, 
            history=chat_history
        )

        # Log the prompt message
        logger.info("Prompt message being sent to model:")
        logger.info(prompt_message)

        body = json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1000,
                "temperature": 0,
                "top_p": 0.9,
                "top_k": 40,
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

        # Log the complete request being sent to Bedrock
        logger.info("Complete request being sent to Bedrock:")
        logger.info(json.dumps(body, indent=2))

        modelId = 'anthropic.claude-3-sonnet-20240229-v1:0'
        accept = 'application/json'
        contentType = 'application/json'
        response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
        
        response_data = json.loads(response["body"].read())
        logger.info("Raw response from Bedrock:")
        logger.info(json.dumps(response_data, indent=2))

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