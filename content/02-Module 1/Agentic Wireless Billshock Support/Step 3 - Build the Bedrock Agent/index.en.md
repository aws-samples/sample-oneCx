---
title : " Billshock Agent build "
weight : 60
---
## In the section you will build the Amazon Bedrock Agent
 
1. On the left side bar of Bedrock console, under **Builder tools** click **Agents**. And then click **Create Agent**. A new window will open, set name as `bill_shock_agent` and leave description field empty. And click **Create**. You will get a green message on the top that **Agent: bill_shock_agent was successfully created** (follow the red arrows and red box in below pictures). 

![agent](/static/module2images/agent.png)
![create agent](/static/module2images/createagent.png)
![agent details](/static/module2images/bsagentcreate.png)
![agent created](/static/module2images/bscreated.png)

2. Under this agent, you will create only one action group. 
3. Scroll down to **Action Groups**. Click **Add** (follow the red arrow in below picture).

![add action group](/static/module2images/ag.png)

4. Billshock action group creation (follow the red arrows and red boxes in below pictures).
      - Set **Enter Action group name:** `billshockagent`
      - Set **Description:** `based on mobile number and secret key it autheticates the custumer. And then check the last month bill with other 2 months`
      - Under **Action group type** select **define with function details**.
      - Under **Action group invocation** select **Select an existing Lambda function**.
      - Under **Select Lambda function** click to open the drop down and select **billshockagent**, keep the **Function version** as **$LATEST**.
      - Under **Action group function 1**, click **JSON Editor** on the right and paste the below json code. Click **Table** to re-verify all the parameters are right then click **Create** at the bottom.

```json
{
  "name": "billshock",
  "description": "Get roaming_eligible value for the customer, get all the paramters",
  "parameters": [
    {
      "name": "customer_mobile_number",
      "description": "customer_mobile_number",
      "required": "True",
      "type": "number"
    },
    {
      "name": "secret_key",
      "description": "secret key of the customer",
      "required": "True",
      "type": "number"
    }
  ],
  "requireConfirmation": "DISABLED"
}
```
-
![add action group](/static/module2images/bsag.png)
![add action group](/static/module2images/bsf.png)
![add action group](/static/module2images/bsp110.png)

5. Congratulations! You have successfully created the action group.  

6. Scroll down to **Select model** , select **Anthropic**, select **Claude 3 Sonnet**, select **on-demand** and click **Apply** (follow the red arrows in below pictures).  

![add action group](/static/module2images/nfta88.png)
![add action group](/static/module2images/nfta89.png)

7. Under **Instructions for the Agent** paste following instruction (follow the red arrow in below picture).

```json
Role: You are a bill analysis agent who analyses customers bill and explain why the bill is high compared to other month.If customer ask for a particular month then just explain that month bill. 
Objective: You should help customers to help them understand in detail why their bill is high 
1. First Step:
    a) Greet the customer with "Welcome to Oktank Billing Support, I am here to help you". This is CRITICAL first step
2. Query Handling:
     a) Never deviate from the main question
     b) Break the main question into subqueries
     c) Use available tools to get answers to subqueries.
3. Ask the customer for mobile number and secret key for authentication and then invoke available tools. Mobile number should be 10 digits and secret key will be 6 digits. Mobile number and secret key can start with any number. So even though customer may not mention explicity mobile number - 1234567890 and secret key- 123456 you should pick-up 10 digit number as mobile number and 6 digits a secret key.
4. Available tools 
- billshockagent - based on mobile number and secret key it autheticates the custumer. And then check the last month bill with other 2 months. Analyse the response from the agent, mention the month and year when you are explaining the bill to the customer so that they understand bill and the associated month and year. Provide detailed response. Always explain the bill to the customer
- billshock-dataroamingplan-kb: If roaming charges are high then use this knowledge base to find the roaming data plans and inform the customer to buy one before travelling abroad. Inform the customer to visit ocktank.com to buy it.
- billshock-disabledataroaming-kb: First ask the customer which mobile the customer has and then search the knowledge base to find the relevant instructions for disabling the data roaming.
5)  Analyse the response from the agent. If the bill is high then always explain the customer why bill is high in detail. Mention the month and year when you are explaining the bill to the customer so that they understand bill and the associated month and year. Provide detailed response. Always explain the bill to the customer
6) If data roaming charges are high then help the customer to disable the data roaming on his mobile phone. First ask the customer which mobile the customer has and then search the knowledge base to find the relevant instructions for disabling the data roaming. 
7) If data roaming charges are high then inform the customer that we have data roaming plans and give the plan details from knowledge base. Inform the customer to visit ocktank.com to buy it.
8) Here is an example
Question: Why my bill is high ?
You will first greet the customer "Welcome to Oktank Billing Support, I am here to help you". You will apologize to the customer and rephrase the question then ask the customer for customer mobile number and secret_key. Successfully Authenticate the customer then break down the query into sub queries and invoke all available tools to provide a coherent answer.  

```
- 
![add kb](/static/module2images/bsp131.png)

8. Under **Additional settings**, go to **User input**, then click **Enabled** (follow the red arrow in below picture).

![add kb](/static/module2images/usinput.png)

9. Do verify following details a) **Agent Name** b) **Agent resource role** c) **Select model** d) **Instruction for the agent** should not be blank e) one action group should be there under **Action Groups** . If all is good then scroll up and click **Save** (follow the red arrows in below pictures).

![add kb](/static/module2images/bsp66.png)
![add kb](/static/module2images/bsp65.png)
![add kb](/static/module2images/bsf2.png) 
![add kb](/static/module2images/bsp140.png) 


10. Now you will add two knowledge bases created in previous sections. 

11. Let's add the first knowledge base. Scroll down to **Knowledge bases** and click **Add**. Select **billshock-disabledataroaming-kb**, under **Knowledge base instructions for Agent** put `knowledge base to find how to disable data roaming on iphone` (follow the red arrows in below pictures).

![add kb](/static/module2images/kb1add.png)
![add kb](/static/module2images/bsp43.png) 

12. Let's add the second and the last knowledge base. Scroll down to **Knowledge bases** and click **Add**. Select **billshock-dataroamingplan-kb**, under **Knowledge base instructions for Agent** put `find all the data roaming plans`(follow the red arrows in below pictures).

![add kb](/static/module2images/kb1add.png)
![add kb](/static/module2images/bsp44.png) 

13. Congratulations! You have added 2 knowledge bases. 

14. Scroll all the way to the bottom to **Advanced Prompts**. Click **Edit**. 

15. Under **Advanced Prompts** (follow the red arrows in below pictures).
 - Click **Orchestration** enable **Override orchestration template defaults**. It will ask to confirm and click **Confirm**. Enable **Activate orchestration template** (if not enabled). 
    -  Under **Configurations** set following values:
        -  **Temperature:** `0`
        -  **Top P:** `0`
        -  **Top K:** `0` 
 - Click **KB response generation** enable **Override knwoledge base response generation template defaults**. It will ask to confirm and click **Confirm**. 
    -  Under **Configurations** set following values:
        -  **Temperature:** `0`
        -  **Top P:** `0`
        -  **Top K:** `0` 
 - Click **Post-processing** enable **Override post-processing template defaults**. It will ask to confirm and click **Confirm**. Enable **Activate post-processing template**. 
     -  Under **Configurations** set following values:
        -  **Temperature:** `0`
        -  **Top P:** `0`
        -  **Top K:** `0` 
        -  **Max completion length:** `4096`
 - At the bottom right corner **Save and exit**. 

![add kb](/static/module2images/ap1.png)
![add kb](/static/module2images/o1.png)  
![add kb](/static/module2images/o2.png) 
![add kb](/static/module2images/bsp51.png)
![add kb](/static/module2images/bsp52.png)
![add kb](/static/module2images/k1.png) 
![add kb](/static/module2images/nfta66.png) 
![add kb](/static/module2images/bsp52.png) 
![add kb](/static/module2images/pp1.png) 
![add kb](/static/module2images/pp1.png) 
![add kb](/static/module2images/bsp54.png) 
![add kb](/static/module2images/bsp55.png) 

16. In the agent console, scroll up and **Save and Exit**. After **Save and Exit**, scroll-up to read the message in the green banner. It is asking to prepare the agent **Agent: bill_shock_agent was successfully updated. Prepare the agent to keep its detail up to date**. 
- On the right side of the console under **Test** you will see **Prepare**. Click **Prepare**. Then you will get one more message in green banner which will say **Agent: bill_shock_agent was successfully prepared** (follow the red arrows in below pictures). 

![add kb](/static/module2images/bsp100.png)
![add kb](/static/module2images/bsp101.png)
![add kb](/static/module2images/bsp102.png)

17. Click **Create Alias**. Set following values: 
    - **Alias name:** `billshock_alias` 
    - **description:** `alias for billshock agent` 
- And click **Create Alias** at the bottom (follow the red arrows in below pictures). 

![add kb](/static/module2images/bsp103.png)
![add kb](/static/module2images/bsca2.png)

###### Note: We have not enabled Bedrock Guardrails but it is highly recommended to enable it and use other best practices when deploying it in production.  

### Congratulations! You have successfully created the agent. Move to Section4 to test the agent. 
