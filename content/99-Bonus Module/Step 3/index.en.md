---
title : "Test the Prompt Flow"
weight : 30
---

## Section 3
## End to End Test of the Prompts, AWS Lambda, and Prompt Flow

Navigate back to the Prompt flow we created and press the Edit in prompt flow builder button

![Navigate to Flow](/static/Module1Images/NavagateToFlowEdit.png)

In the Test Prompt flow window on the right of the page, enter "bill shock" in the bottom panel.  This will be the value passed into the Flow input block to:

1.  Generate the contact center transcript for the topic of bill shock
2.  Analyze and parse the transcript to identify the Issues, Actions, and Outcomes of the conversation
3.  Use the analysis as input to the AWS Lambda to then post to the Connected Customer Journey solution to track all of the sub-journeys for the customer
4.  We will see the result of the transaction from the Connect Customer Journey API

Give it a try!

![Bill Shock](/static/Module1Images/TestPromptInputA.png)

Let's take a look under the hood to see what the Prompt Flow orchestrated to run two Prompts and one AWS Lambda to achieve the outcomes of:

1.  Create a synthetic contact center transcript based on the topic of "bill shock"
2.  Analyze the transcript to identify Issues, Actions, Outcomes and format the output in a structure that the Connected Customer Journey solution in Module 2 expects
3.  Submit the formatted analysis results to the AWS Lambda to then send to the Connected Customer Journey's API
4.  Show the Trace results of each step and the time it took for each to execute

Here is a walk-through of what you should see when running the Prompt Flow and selecting the Show Trace option:

![Success](/static/Module1Images/Trace1.png)
![Success](/static/Module1Images/Trace2.png)
![Success](/static/Module1Images/Trace3.png)
![Success](/static/Module1Images/Trace4.png)
![Success](/static/Module1Images/Trace5.png)
![Success](/static/Module1Images/Trace6.png)
![Success](/static/Module1Images/Trace7.png)
![Success](/static/Module1Images/Trace8.png)

This level of visibility will help you quickly validate what your Prompts, AWS Lambda Functions, and all other Nodes in the Prompt Flows are using for input, delivering for output, and how the Prompt Flow orchestrates per the visual editor.

And now for a peek at Art of the Possible of what you can do with Amazon Bedrock text inference models for much deeper, broader call, chat, and other digital channel interaction analytics!

Navigate to the following URLs for a quick look at two publicly available projects, Live Call Analytics and Post Call Analytics, where can deploy the projects in about 45 minutes each and customize to mee your specific needs from there:

https://aws.amazon.com/blogs/machine-learning/post-call-analytics-for-your-contact-center-with-amazon-language-ai-services/

https://aws.amazon.com/blogs/machine-learning/live-call-analytics-and-agent-assist-for-your-contact-center-with-amazon-language-ai-services/

We accomplished a LOT in a very short time in Module 1:

1. We built Amazon Bedrock Prompts in Prompt Management
2. We leveraged a pre-deployed AWS Lambda to interface to the Module 2 Connected Customer Journey API
3. We built an Amazon Bedrock Prompt Flow
4. We tested the Prompt Flow and viewed the trace details to see:
    a. Generative AI-created transcript to match the "bill shock" scenario we provided as input
    b. Generative AI-analyzed transcript to identify:
        1. Issues
        2. Actions
        3. Outcomes
    c. AWS Lambda execution to push the analytics outcomes to the API

We hope this inspires you to ask, "What Prompts, Prompt Flows, Amazon Bedrock models shall I use for A, B, C - Z use cases . . . ?" 

Thanks for completing the Bonus section!