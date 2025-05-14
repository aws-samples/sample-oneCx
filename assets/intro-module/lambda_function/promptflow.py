import json
import logging
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def invoke_bedrock_prompt_flow(flow_id, flow_alias_id, payload):
    """
    Invokes an Amazon Bedrock prompt flow for offer eligibility checking.

    Args:
    flow_id (str): The ID of the prompt flow to invoke.
    flow_alias_id (str): The alias ID of the prompt flow.
    customer_journey_data (str): The customer journey data as a string.

    Returns:
    dict: The output of the prompt flow.
    """
    try:
        # Create a Bedrock Agent Runtime client
        client_runtime = boto3.client('bedrock-agent-runtime')
        # Invoke the prompt flow
        response = client_runtime.invoke_flow(
            flowIdentifier=flow_id,
            flowAliasIdentifier=flow_alias_id,
            inputs=[
                {
                    "content": {
                        "document": json.dumps(payload)
                    },
                    "nodeName": "FlowInputNode",
                    "nodeOutputName": "document"
                }
            ]
        )

        result = {}

        # Process the streaming response
        for event in response.get("responseStream"):
            result.update(event)

        # Check if the flow completed successfully
        if result['flowCompletionEvent']['completionReason'] == 'SUCCESS':
            print("Prompt flow invocation was successful! The output of the prompt flow is as follows:\n")
            print(result['flowOutputEvent']['content']['document'])
            return result['flowOutputEvent']['content']['document']
            
        else:
            print("The prompt flow invocation completed because of the following reason:", 
                  result['flowCompletionEvent']['completionReason'])
            return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def handler(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))

    try:
        # The event structure might vary depending on how it's passed through EventBridge and Step Functions
        # You might need to adjust this part based on the actual event structure you receive
        if 'detail' in event:
            rds_event = event['detail']
        else:
            rds_event = event

        # Extract the notification payload
        if 'Message' in rds_event:
            payload = json.loads(rds_event['Message'])
        else:
            payload = rds_event

        # Log the extracted payload
        logger.info("Extracted payload: " + json.dumps(payload, indent=2))

        flow_id = '868FQWOMLU'
        flow_alias_id = 'ZANW99C2CC'

        # Invoke the Bedrock Agent flow
        invoke_bedrock_prompt_flow(flow_id, flow_alias_id, payload )

        return {
            'statusCode': 200,
             'body': json.dumps({
                'payload': payload
            })
        }
    except Exception as e:
        logger.error(f"Error processing event: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }