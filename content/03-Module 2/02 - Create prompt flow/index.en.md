---
title : "Create the product recommendation Flow"
weight : 20
---

In this section you continue on to create the flow using the the offer eligibility prompt, customer segmentation agent, and product recommendation agent that we examined in the previous section.

**Step 1:** Create the flow for product recommender

a. Click on the **Flows** link from the left hand panel

![Edit in Agent Builder Customer Segmentation](/static/Module3/images/prompt-flow-lefthandpanel.png)

Click on the **Creat Flow** button. 

![Create prompt flow](/static/Module3/images/prompt-flow-create-flow.png)

b. Enter the name as `ProductRecommender` and description as `This flow recommends products for a given customer`.

![Create prompt flow fields](/static/Module3/images/prompt-flow-create-fields.png)

c. In the service role name field, select `Create and use a new service role`.

d. Click on **Create**.

This should take you to the following screen for the flow builder.

![Prompt flow builder](/static/Module3/images/prompt-flow-builder.png)

The flow builder screen has 3 parts:

1. The nodes and configuration pane - This is found on the left side of the screen.
2. The flow canvas - This is the canvas in the middle of the screen.
3. The test flow pane - This is found on the right side of the screen.

Now we shall start adding nodes and links to the flow in the following steps.

---

**Step 2** Add a lambda function to get the customer journey data.


a. From the flow builder node list on the left, Drag and drop the **Lambda function** node on the canvas. 

![Drag and Drop lambda](/static/Module3/images/prompt-flow-draganddrop-lambdafunction.png) 

Click on it and then on the configure screen, provide the following details:



**Node name** - :code[`getCustomerJourney`]{showCopyAction=true}

**Lambda function** - choose :code[**GetCustomerJourney**]{showCopyAction=true}, leave the version as $LATEST, leave the input fields as it is, in the **output** field choose **Object** as the **Type**.

![Configure get customer journey lambda](/static/Module3/images/prompt-flow-getcustomerjourney-lambda.png) 


b. Click on the link between the flow input and the flow output and then hit backspace on your keyboard to delete it.

![Configure get customer journey lambda](/static/Module3/images/prompt-flow-delete-link.png) 


c. Click on the Flow input node connector and connect it to the getCustomerJourney lambda function Input node connector.

![Edit in Agent Builder Customer Segmentation](/static/Module3/images/prompt-flow-add-customer-journey-lambda.png) 


:::alert{header="Important Tip" type="alert"}
Click on this button at the bottom right of the screen to rearrange the flow properly and to resize the nodes for ease on navigation on the canvas.

![Prompt flow rearrange nodes](/static/Module3/images/prompt-flow-rearrangenodes.png)


This should result in the nodes rearranging as below:

![Prompt flow rearrange nodes](/static/Module3/images/prompt-flow-rearrangedicons.png)

You should also close the **Test flow** pane to create more space on the canvas to work with nodes and links.

![Close test flow](/static/Module3/images/prompt-flow-close-test-flow.png)

The resultant screen should look like the below:

![Closed test flow panel](/static/Module3/images/prompt-flow-closed-testpanel.png)
:::

---

**Step 3** Add the offer eligibility checker prompt.

a. On the prompt builder screen, drag and drop the **Prompts** node on the canvas. 

![Prompt flow add prompt](/static/Module3/images/prompt-flow-add-prompt.png)


Click on it and then on the configure screen, provide the following details:
**Node name** - :code[`OfferEligibilityChecker`]{showCopyAction=true}

**Prompt** - :code[OfferEligibilityChecker]{showCopyAction=true}

**Input** - change the Type field to `Object`.


![Prompt flow add prompt](/static/Module3/images/prompt-flow-configure-prompt.png)



![Prompt flow add prompt](/static/Module3/images/prompt-flow-prompt-inputobjecttype.png)



Leave the rest of the fields as they are.

b. Connect the output node connector of the getCustomerJourney lambda function node to the input node connector of the OfferEligibilityChecker Prompt node. 


![Prompt for eligibility check](/static/Module3/images/prompt-flow-offereligibilitychecker-prompt.png) 


c. Connect the output node connector of the prompt node to the Flow output node Input node connector.


![Prompt for eligibility check output](/static/Module3/images/prompt-flow-prompt-outputconnect.png) 


Rearrange the nodes for ease of navigation:


![Prompt for eligibility check output reaarange](/static/Module3/images/prompt-flow-prompt-output-rearrange.png) 


:::alert{header="Important tip" type="alert"}
Click on **Save** to save the flow so that you do not loose your work in case of any inadvertent issues (for example laptop restarting). You should see confirmation of the save as follows at the top of the screen:

![Save prompt flow](/static/Module3/images/prompt-flow-intermediate-save.png)

You will also see the following warning appear about policies remaining for nodes that are deleted - This warning does not apply to you as no nodes have been deleted, nor are we focussed on this issue as part of this workshop.

![Save prompt flow warning](/static/Module3/images/prompt-flow-save-warning.png)


:::


Rename the output node to **OfferEligibilityCheckOutput**


![Save prompt flow warning](/static/Module3/images/prompt-flow-ofeloutput.png)


---

**Step 4** Add a lambda function to extract the offer eligibilty payload.

a. On the flow builder screen, Drag and drop the **Lambda function** node on the canvas. Click on it and then on the configure screen, provide the following details:

**Node name** - :code[`OfferEligibilityExtractor`]{showCopyAction=true}

**Lambda function** - choose :code[OfferEligibilityExtractor]{showCopyAction=true}, leave the version as $LATEST, leave the input fields as it is, in the **output** field choose **Object** as the **Type**.


![Offer eligibility extractor lambda](/static/Module3/images/prompt-flow-offereligibilityextractorlambda.png) 


b. Click on the output node connector of the OfferEligibilityChecker node and connect it to the OfferEligibilityChecker lambda function's Input node connector. 


![Connect offer elgbcheck to offerextratctor lambda](/static/Module3/images/prompt-flow-connect-prompt-to-lambda.png)


d. Click on the rearrange icons button to rearrange the nodes and connectors so that it renders well on the canvas.


![Connect offer elgbcheck to offerextratctor lambda](/static/Module3/images/prompt-flow-oex-rarrange.png)

---

**Step 5** Add a condition node to check if the offer eligibilty is True or False

a. On the prompt builder screen, drag and drop the **Condition** node on the canvas.


![Add condition node](/static/Module3/images/prompt-flow-add-condition.png)



Click on it and then on the configure screen, provide the following details:

**Node Name** - :code[`OfferEligibilityCheckerCondition`]{showCopyAction=true}

**Input Name** - :code[`offerEligible`]{showCopyAction=true}

**Input Type** - :code[`Boolean`]{showCopyAction=true}

**Expression** - :code[`$.data.offer_eligible`]{showCopyAction=true} (this is an inbuilt json field extractor expression that extracts the value of the offer_eligible field from the json output of the offerEligibilityExtractor lambda function).

**Condition** - In the condition field enter :code[`offerEligible == true`]{showCopyAction=true}.


![Add condition node on the prompt flow](/static/Module3/images/prompt-flow-ofecheck-condition.png)



b. Connect the output of the offerEligibilityExtractor lambda function node to the input of the condition node.


![Add condition node on the prompt flow](/static/Module3/images/prompt-flow-connect-condition.png)



::alert[Click on **Save** to save your work]


---

**Step 6** Add a flow output node for observability of the offerEligibilityExtractor output

a. Drag and drop the output node on the canvas.


![Add condition node output ofe](/static/Module3/images/prompt-flow-add-flow-output-ofe.png)


b. Name the node :code[`offerEligibilityExtractorOutput`]{showCopyAction=true}.

Configure the output nodes' input field data type as **Object**


![Add condition node output ofe](/static/Module3/images/prompt-flow-ofeoutput-config.png)


c. Connect the output of the `OfferEligibilityExtratcor` lambda node to the Flow output input.


![Connect lambda output to flow output](/static/Module3/images/prompt-flow-connect-ofelambda-output.png)


d. Connect the **"If conditions are false"** output of the condition node to the **OfferEligibilityExtractorOutput** node


![Connect condition false output to flow output](/static/Module3/images/prompt-flow-connect-condition-to-output.png)


---

**Step 7** Add a Lambda function node to convert the json output from the OfferEligibilityExtractor node to string.

a. Drag and drop the lambda function node on the canvas.

b. Provide the node name as :code[`jsonToString`]{showCopyAction=true}, choose :code[`JsonToString`]{showCopyAction=true} in the Lambda function field, choose `object` in the input type field.


![Json to String Lambda function](/static/Module3/images/prompt-flow-jsontostring-lambda.png)


c. Connect the output node connector of the OfferEligibilityExtractor lambda function node to the input of the jsonToString.


![ofel to Json to String Lambda connect](/static/Module3/images/prompt-flow-ofel-connect-json2string.png)


d. Connect the True output node connector of the OfferEligibilityCheckerCondition to the jsonToString node input.


![ofel condition true to Json to String connect](/static/Module3/images/prompt-flow-connect-ofex-true-json2string.png)



::alert[Click on **Save** to save your work]


---

**Step 8** Add a Agent node to derive customer segments from the customer journey data.

a. Drag and drop the Agent node on the canvas.


![Add agent](/static/Module3/images/prompt-flow-add-agent.png)


b. Provide the node name as :code[`customerSegmentFinder`]{showCopyAction=true}, Agent as :code[`CustomerSegmentationAgent`]{showCopyAction=true}, and Agent Alias as `AgentTestAlias`.


![Add customer segemntfinder agent config](/static/Module3/images/prompt-flow-customersegmentfinder-agent-config.png)


Make sure to uncheck the use of optional prompt attributes and session attributes as shown below:


![Add customer segemntfinder agent config](/static/Module3/images/prompt-flow-uncheck-optional-attributes.png)


c. Connect the output of the `jsonToString` lambda function node to the input of the `customerSegmentFinder` agent node.

![Connect json2string with customersegmentfinder agent](/static/Module3/images/prompt-flow-connect-json2string-agent.png)

---

**Step 9** Add a Flow output node to record the output of the customer segement finder agent.

a. Drag and drop the output node on the canvas.

b. Name the node :code[`customerSegementationOutput`]{showCopyAction=true}.


![Customersegmentfinder agent output](/static/Module3/images/prompt-flow-customer-segmentation-output.png)


c. Connect the output of the `customerSegmentFinder` agent to the `customerSegementationOutput` Flow output node input.

![Connect ustomersegmentfinder agent output](/static/Module3/images/prompt-flow-connectcsfagent-output.png)


::alert[Click on **Save** to save your work]


---

**Step 10** Add an agent node to create product recommendations, rank them, and derive offer negotiation band.

a. Drag and drop the Agent node on the canvas.

b. Provide the node name as :code[`ProductRecommender`]{showCopyAction=true}, Agent as :code[`ProductRecommendationAgent`]{showCopyAction=true}, and Agent Alias as :code[`AgentTestAlias`]{showCopyAction=true}.


![Add productrecommender agent](/static/Module3/images/prompt-flow-productrecommender-agent-add.png)


c. Connect the output of the `customerSegmentFinder` agent node to the input of the `ProductRecommender` agent node.

![Add product recommender agent connection](/static/Module3/images/prompt-flow-connect-csfa-prrecagent.png)

---

**Step 11** Add an output node to record the output of the productRecommender agent.

a. Drag and drop the output node on the canvas.

b. Name the node :code[`productRecommenderOutput`]{showCopyAction=true}.

c. Connect the output of the `productRecommender` agent to the `customerSegementationOutput` Flow output node input.

![Add product recommender agent output](/static/Module3/images/prompt-flow-productRecommenderOutput-agent.png)


::alert[Click on **Save** to save your work]


---


The final flow should look as follows:

![Add product recommender agent output](/static/Module3/images/prompt-flow-final.png)

Click on **Save**. This should return a notification as shown below:

![Add product recommender agent output](/static/Module3/images/prompt-flow-save-confirmation.png)


**Congrats, you have now created your product recommender flow successfully.** In the next section you will test this flow from the Amazon Bedrock console.




