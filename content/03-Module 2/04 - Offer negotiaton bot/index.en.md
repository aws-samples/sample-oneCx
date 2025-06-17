---
title : "Examine and test the offer negotiation bot"
weight : 40
---

In this section we shall test how an Amazon Bedrock powered chatbot can use the offers and negotiation bands recommended by the product recommender to converse with a customer who is looking to close a deal on an upgrade offer provided to them.

::alert[This section assumes that the product recommender flow has been run successfully for a customer. We start in this module with the offers that have been recommended to the customer.]

Below is an architecture diagram that shows how the data flow:


:image[Workshop Image]{src=/static/Module3/images/tlc302-productreco-architecture.png width = 900 height = 500 disableZoom=true}


Please follow the below steps to explore the pre-created resources and then to test the offer negotiator chatbot - 

**Explore the AWS lambda function  that calls Bedrock**

a. Search for 'lambda' on the search bar

b. Search for the function name - :code[OfferNegotiator]{showCopyAction=true}

c. Examine the code - The code does the following:

:::code{showCopyAction=false showLineNumbers=false language=python}
- The code uses an AI language model (Anthropic's Claude) to analyze the user's intent in each message, categorizing it as 'accept', 'reject', 'negotiate', 'info_request', or 'other'.
- If the intent is 'negotiate', the code tries to extract a price offer from the user's message using regular expressions.
- Based on the intent and price offer (if any), the code calculates an appropriate discount percentage for the current offer, up to a maximum discount limit set for each product package.
- The maximum discount percentage and initial price vary for different product packages ('basic', 'premium', and 'ultimate').
- If the user rejects or negotiates, the code increases the discount by a small amount (5%) for the next offer, up to the maximum discount limit.
- If the user accepts, the code confirms the last offered price for the selected product package.
- If the user requests more information, the code provides detailed package features and the current offer price.
- The code generates responses accordingly, prompting the user to accept or negotiate further based on the current offer price.
:::

**Test the chatbot**

a. Navigate to the AWS CloudFormation console.

b. Search and open the stack named "frontend"

c. Go to the outputs tab.

Copy the value of the following parameters:
**ReactAppApiEndpointxxxxxx** - This is the url of OneCX, where you will find the offer negotiator chatbot
**UiUsername** - User name for the portal
**UiPassword** - Password for the portal

::alert[For detailed instructions with screenshots for retrieving the above information, please refer to the **Introduction module - Visualize and Summarize a Customer Journey** section]

d. Click on the **Offer Negotiator** button

This screen shows the offers that have been provided to a particular customer as a result of the previous Product Recommender flow having run successfully.

![Offer Negotiator button](/static/Module3/images/offer-negotiator-initial-screen.png)

e. You can then have a conversation to negotiate the price as follows:

![Offer Negotiator bot](/static/Module3/images/offer-negotiator-bot.png)

As you see in the above conversation, the bot assesses the users messages to determine what the user would like to do. The bot then uses the business logic defined using natural language or low-code rules to provide a discount on the offered price if possible. This solution can also be extended to offer add-ons and other services as part of the upgrade negotiation.

**Congratulations** You have now completed this workshop!!