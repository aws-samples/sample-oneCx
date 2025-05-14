---
title : "Test your product recommendation flow"
weight : 30
---

In this section you test the flow using the Amazon bedrock console. The objective of this section is to test that the flow executes and produces the offer eligibility check, customer segmentation, and product recommendations as expected.


**Step 15** Test your flow

a. Enter the following json payload in the **Test Flow** window on the right of the Prompt flow builder page.

`{"customer_id":14}`


![Test prompt flow](/static/Module3/images/prompt-flow-test-prompt-flow.png).


b. The processing of the flow goes through a number of LLM inferences so it can take a upto 2 minutes to complete. You should start seeing intermediate outputs from the flow in a few seconds as follows:

**Offer eligibility check output**


![Test prompt flow offer eligibility output](/static/Module3/images/prompt-flow-offereligibilitycheck-promptflowoutput.png)


The output shows that the customer is eligible for an offer. It also shows the reasons because of which the customer has been deemed to be eligible for the offer.


You can check the trace of the flow by clicking on the **Show trace** link as shown below. Trace is a log that Bedrock produces that allows developers to check the sequence of events that the flow executed.


![Test prompt flow offer eligibility output](/static/Module3/images/prompt-flow-offereligibility-showtrace.png)


The trace output must appear as follows. As you notice, the trace shows the time it took to execute each step and the logged output at each step as well. This is really useful while debugging issues you may face during development and testing.


![Test prompt flow offer eligibility output](/static/Module3/images/prompt-flow-trace-output.png)


Next, examine the output of the customer segmentation:


![Test prompt flow offer eligibility output](/static/Module3/images/prompt-flow-customer-segmentation-promptflowtestoutput.png)


The customer segmentation agent classifies the customer based on a few parameters - spend level, product impressions, and network experience. The segmentation configuration is configurable. This is the power of using generative AI for customer segmentation. You can define by what parameters you would like to segment your customer base in natural language or semi-structured formats like json. The large language model uses this to look at the the customer's journey and then creates a customer segement profile of the customer at that point in time.

Next, examine the output of the product recommendation:


![Test prompt flow offer eligibility output](/static/Module3/images/prompt-flow-productrecommendation-promptflowoutput.png)


The product recommendation agent looks at the customer segmentation output and the product segment mapping to analyze and provide a ranked list of products. The agent also provides the reasons for recommending the product. Next, it looks at the customer profile which contains information regarding the customers churn potential, lifetime value and other demographic information to decide on the offer negotiation band. This output can be used by a GenAI chatbot to have a fully self served offer negotiation chat.

**Congrats, you have now completed this section and have tested the output of your product recommendation flow successfully.**