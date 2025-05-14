---
title : "Build Prompt Flow in Amazon Bedrock Prompt Flows"
weight : 20
---

## Section 2
## Build Prompt Flow in Amazon Bedrock Prompt Flows

In the search bar at the top of the AWS Console, type Amazon Bedrock and click on the link for Amazon Bedrock

![Prompt Flows](/static/Module1Images/OpenAmazonBedrockConsole.png)

On the left side of the page, select the Prompt flows link

![Prompt Flows](/static/Module1Images/SelectPromptFlow.png)

Press the Create prompt flow button.  Note:  there are two create prompt flow buttons - either will work!

![Create Prompt Flow](/static/Module1Images/CreatePromptFlow.png)

Fill in the fields as shown below.  

**Name**: `TLC302PromptFlow`

**Description**: `This flow will use two prompts and the AWS Lambda to populate the Connected Customer Journey solution with customer events from a contact center transcript.`

**Service Role Name**: Choose `Create and use a service role`

Press the Create button when all is entered accurately.

![Config Flow](/static/Module1Images/ConfigFlow.png)

You will then see the following

![Flow Defined](/static/Module1Images/FlowSuccessDefined.png)

Click on the connection line between the Flow input and Flow output blocks and push the backspace key on your keyboard to remove the connection as shown below.

![Remove Connection](/static/Module1Images/RemoveConnector.png)

Click the Nodes Tab on the left of the page, and then drag two Prompt blocks and one Lambda function block as shown below.  Don't worry about the layout or the connections, yet - we will configure those!

![Drag Blocks](/static/Module1Images/DragBlocks.png)

Now, click on the top Prompts block in the middle of the page and configure it as below.  **Note**:**  this will use one of the Prompts we created at the beginning of the module, and you will now see a connection point on the left of the block where we can connect the input block in the next step.

![Create Transcript Block](/static/Module1Images/CreateTranscriptBlock.png)

Next, let's connect the Flow input block to the configured Prompt block, and then configure and connect the second Prompt block as shown here

![Create Analyze Block](/static/Module1Images/CreateAnalyzeBlock.png)

We have pre-deployed the AWS Lambda to be used in this Prompt Flow.  The key part of the code to note is below.  The code is showing how the AWS Lambda is formatting the results from the previous Prompt block to then send to the API used to track the customer journey (details in Module !!) The below is just to explain what the AWS Lambda is doing - do not worry about taking action on this code snippet below:

:::code{showCopyAction=true showLineNumbers=true language=python}
def lambda_handler(event, context):
    print("Lambda function started")
    print(f"Received event: {json.dumps(event, indent=2)}")

    try:
        # Extract the relevant information from the input
        input_data = json.loads(event['node']['inputs'][0]['value'])
        transcript_analysis = input_data['transcript_analysis']

        # Create the JSON object expected by the API
        api_payload = {
            "event_type_id": "1",
            "customer_id": transcript_analysis['customer_id'],
            "event_id": transcript_analysis['call_id'],
            "event_description": transcript_analysis['summary'],
            "timestamp": transcript_analysis['date'],
            "additional_attributes": {
                "duration": transcript_analysis['duration'],
                "agent_id": transcript_analysis['agent_id'],
                "issues": transcript_analysis['issues'],
                "actions": transcript_analysis['actions'],
                "outcomes": transcript_analysis['outcomes']
            }
        }
:::

Configure the AWS Lambda block as shown below - choose the lambda function shown from the list.  

Choose the output node type as **Object**

Choose the input data type of the Output node as **Object**

![Config Lambda](/static/Module1Images/PromptFlowLambdaFunction.png)

Connect the lambda node to the output node. The click **Save**. The final prompt flow should looks as below.

![Module 1 final prompt flow](/static/Module1Images/SavePromptFlow.png)

Now that we have configured the two Prompts, the AWS Lambda, and the Prompt Flow, we are ready to test!
