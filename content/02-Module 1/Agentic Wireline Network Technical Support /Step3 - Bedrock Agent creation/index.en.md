---
title : " Amazon Bedrock Agent creation"
weight : 110
---
## In the section we have pre-built an Amazon Bedrock Agent with five action groups for you. You will a) review the agent configurations b) add knowledge bases c) configure advance prompts 

 1. On the left side bar of Bedrock console, click **Agents**. Then click **network_fault_troubleshooting_agent**.  

![agent](/static/module2images/agent.png)
![agent](/static/module2images/nfta81.png)

  - Then click **Edit in Agent Builder**. Under **Agent details** review **Agent name:** `network_fault_troubleshooting_agent` 

![agent](/static/module2images/nfta155.png)

  - Under **Select model:** review `Claude 3 Sonnet v1` (follow the red arrows in below pictures). 

![agent](/static/module2images/nfta130.png)

2. Under **Agent resource role**, click **Create and use a new service role**. Scroll up and click **save** (follow the red arrow in below picture).

![agent](/static/module2images/nfta210.png)


::::expand{header="In this agent, five action groups are pre-built. After you complete the workshop, you should review them to understand what is the role of each action group" defaultExpanded=false}

3. Scroll down to **Action Groups** (follow the red box in below picture).

![add kb](/static/module2images/nfta156.png) 

4. Now let's review the first action group configurations - billstatus
 - Click **billstatus**
 - **Enter Action group name:** `billstatus`
 - **Description:** `use this agent to check whether customer has paid last month bill or not` 
 - **Action group type:** **Define with function details**
 - **Action group invocation:** **Select an existing Lambda function**, Lambda function name is **techbillpaymentstatusagent**, **Function version** as **$LATEST**

![add action group](/static/module2images/agd.png)

 - Under **Action group function 1: billstatus**, click **JSON Editor** on the right and review the json block
    - If everything looks fine then click **cancel** at the bottom (follow the red arrows in below pictures). 

:::code{showCopyAction=false showLineNumbers=false language=json}
{
            "name": "billstatus",
            "description": "get the bill payment status of the last month for the customer",
            "parameters": [
            {
                  "name": "customer_id",
                  "description": "This is the customer id of the customer",
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
:::

![add action group](/static/module2images/nfta83.png)


5. Now let's review the second action group configurations- customer_authentication
 - Click **customer_authentication**
 - **Enter Action group name:** `customer_authentication`
 - **Description:** `authenticates the customer with customer_id and secret_key` 
 - **Action group type:** **define with function details**
 - **Action group invocation:** **Select an existing Lambda function**, Lambda function name is **techcustomerauthagent**, **Function version** as **$LATEST**

![add action group](/static/module2images/ags1.png)

 - Under **Action group function 1: customer_a**, click **JSON Editor** on the right and review the json block.
    - If everything looks fine then click **cancel** at the bottom (follow the red arrows in below pictures).

:::code{showCopyAction=false showLineNumbers=false language=json}
{
            "name": "customer_authentication",
            "description": "matches customer_id and secret_key and if they match then it returns customer is authenticated",
            "parameters": [
            {
                  "name": "customer_id",
                  "description": "This is the customer id of the customer",
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
:::

![add action group](/static/module2images/nfta84.png)

6. Now let's review the third action group configurations- modem_status
 - Click **modem_status**
 - **Enter Action group name:** `modem_status`
 - **Description:** `based on the customer_id returns the modem status for the customer` 
 - **Action group type:** **define with function details**
 - **Action group invocation:** **Select an existing Lambda function**, Lambda function name is **techmodemstatusagent**, **Function version** as **$LATEST**

![add action group](/static/module2images/ags2.png)

 - Under **Action group function 1**, click **JSON Editor** on the right and review the json block.
    - If everything looks fine then click **cancel** at the bottom (follow the red arrows in below pictures).

:::code{showCopyAction=false showLineNumbers=false language=json}
{
            "name": "modemstatus",
            "description": "based on the customer_id returns the modem status for the customer",
            "parameters": [
            {
                  "name": "customer_id",
                  "description": "This is the customer id of the customer",
                  "required": "True",
                  "type": "number"
            }
            ],
            "requireConfirmation": "DISABLED"
}
:::


![add action group](/static/module2images/nfta85.png)

7. Now let's review the fourth action group configurations- node_status
 - Click **node_status**
 - **Enter Action group name:** `node_status`
 - **Description:** `check and return the node status for a particular customer` 
 - **Action group type:** **define with function details**
 - **Action group invocation:**  **Select an existing Lambda function**, Lambda function name is **technodestatusagent**, **Function version** as **$LATEST**

![add action group](/static/module2images/ags3.png)

 - Under **Action group function 1: node-statu**, click **JSON Editor** on the right and review the json block.
    - If everything looks fine then click **cancel** at the bottom (follow the red arrows and red boxes in below pictures).

:::code{showCopyAction=false showLineNumbers=false language=json}
{
            "name": "node-status",
            "description": "check and return the node status for a particular customer",
            "parameters": [
            {
                  "name": "customer_id",
                  "description": "This is the customer id of the customer",
                  "required": "True",
                  "type": "number"
            }
            ],
            "requireConfirmation": "DISABLED"
}
:::

![add action group](/static/module2images/nfta86.png)

8. Now let's review the fifth and the last action group configurations - speedstatus
 - Click **speedstatus**
 - **Enter Action group name:** `speedstatus`
 - **Description:** `check the current speed of user` 
 - **Action group type:** **define with function details**
 - **Action group invocation:** **Select an existing Lambda function**, Lambda function name is **techspeedstatusagent**, **Function version** as **$LATEST**

![add action group](/static/module2images/ags4.png)

 - Under **Action group function 1: speedstatu**, click **JSON Editor** on the right and review the json block. 
    - If everything looks fine then click **cancel** at the bottom (follow the red arrows in below pictures).

:::code{showCopyAction=false showLineNumbers=false language=json}
{
  "name": "speedstatus",
  "description": "check the current speed of user",
  "parameters": [
    {
      "name": "customer_id",
      "description": "This is the customer id of the customer",
      "required": "True",
      "type": "number"
    }
  ],
  "requireConfirmation": "DISABLED"
}
:::

![add action group](/static/module2images/nfta87.png)

9. Congratulations! You have reviewed all five action groups.

  ::::

10. Under **Instructions for the Agent** review the following instruction (follow the red arrow in below picture).

:::code{showCopyAction=false showLineNumbers=false language=json}
Role: Home broadband network troubleshooting agent. 
Objective: You should help customers to troubleshoot network issues. 
1. First Step:
    a) Greet the customer with "Welcome to Oktank Technical Support, I am here to help you". This is CRITICAL first step
2. Query Handling:
     a) Never deviate from the main question
     b) Break the main question into subqueries
     c) Use available tools to get answers to subqueries.
4. Authentication:  
     a) Ask the customer to provide customer_id (10 digits) and secret_key (6 digits)
     b) Never assume these credentials
     d) Do not invoke any other agents until the customer provides these details and is successfully authenticated. 
5. Available Tools: 
     a) customer_authentication agent: Authenticates customer with customer_id and secret_key. If they don't match, inform the customer. DO NOT INVOKE ANY OTHER AGENTS UNLESS CUSTOMER IS SUCCESSFULLY AUTHENTICATED. 
    b) billstatus agent: Checks if the customer has paid last month's bill.Uses customer_id and secret_key.Non-payment reduces the network speed but never cuts off the network or it will never make the modem down. 
     c) speedstatus agent: Checks current speed based on current month and customer_id. Returns new_upload_speed, new_download_speed, allowed_upload_speed, allowed_download_speed (all in Mbps). If new speeds are lower than allowed speeds, explain the reason
    d) modem_status agent: Checks modem status based on customer_id. If modem is down, internet/network won't work
    e) node_status agent: Checks node status based on customer_id. If node is down, internet won't work
     f) Knowledge Bases:
      - billpayment-kb: Contains broadband bill payment methods for iOS, Android, macOS, and Windows. Always ask the customer which device type they have now- windows, macOS, Andriod or iOS. Based on the device type, provide the relevant step by step instructions. 
      - modem-troubleshooting: Used for troubleshooting customer modem issues. don't provide all steps at once
6. Agent Invocation Rules:
    a) Pass actual customer_id and secret_key to all agents
    b) Pass all responses from agents to the next agent
7. Response Generation:
     a) Do not use your own knowledge to answer queries
     b) Provide comprehensive, coherent responses based on agent findings
8. Troubleshooting Logic:
    a) If speedstatus agent reports slow speed, check bill payment status. Remember non-payment results in slow network speed and it will never make the network down. Explain the old and new speed
    b) Network won't work if modem or node is down (or both)
    c) Bill non-payment only reduces network speed, never causes modem to go down or never make the network down
9. Modem Troubleshooting:
    a) Ask if the customer is ready to troubleshoot
    b) Guide customer step-by-step, don't provide all steps at once
    c) Refine steps based on customer feedback
10. Bill Payment 
    a) If there is a brand (Samsung) which manufactures mobile, computers and tablets then ask for more details like its a mobile, tablet or computer. don't provide all steps at once.
11. System Update Times:
     a) After bill payment confirmation: Up to 1 hour for backend system update
    b) After successful modem troubleshooting: Up to 1 hour for backend system update
12. Node Failure:
      a) No troubleshooting required from customer side
13. Remember:
     a) Use knowledge bases and agents for information, not your own knowledge
     b) Provide coherent, comprehensive responses based on agent findings
    c) Guide customers through modem troubleshooting only when necessary
14. Here is an example
Question: Why my network is down?
You will first greet the customer "Welcome to Oktank Technical Support, I am here to help you". You will apologize to the customer and rephrase the question then ask the customer for customer_id and secret_key. Successfully Authenticate the customer then break down the query into sub queries and invoke all available tools to provide a coherent answer.  
:::


![add kb](/static/module2images/nfta212.png) 

11. Under **Additional settings**, go to **User input**, then click **Enabled** (follow the red arrow in below picture).

![add kb](/static/module2images/usinput.png)

12. If all is good then scroll all the way up and click **Save** (follow the red arrow in below picture).

![add kb](/static/module2images/nfta157.png)

13. Now we will add two knowledge bases created previously. 
14. Let's add the first knowledge base. Scroll down to **Knowledge bases** and click **Add**. Select **modemtroubleshoot-kb**, under **Knowledge base instructions for Agent** put :code[this knowledge base is used for troubleshooting customer modem if modem is not working. Provide provide step by step troubleshooting]{showCopyAction=true} (follow the red in arrows below pictures).

![add kb](/static/module2images/kb1add.png)

![add kb](/static/module2images/kb1details.png) 

15. Let's add the second and the last knowledge base. Scroll down to **Knowledge bases** and click **Add**. Select **billpayment-kb**, under **Knowledge base instructions for Agent** put :code[This knowledge base contains broadband bill payment for IOS, Android, MacOS and Windows. Ask the customer which device they use then provide step by step help to the users.]{showCopyAction=true} (follow the red arrows below pictures).

![add kb](/static/module2images/kb1add.png)

![add kb](/static/module2images/kb2details.png) 

16. Congratulations! You have added 2 knowledge bases. 

17. Scroll all the way to the bottom to **Orchestration strategy** (earlier it was called as Advanced Prompts). Click **Edit**. 

![add kb](/static/module2images/ap1.png)

18. Under **Orchestration strategy** (follow the red arrows in below pictures).

  - Click **Orchestration** enable **Override orchestration template defaults**. It will ask to confirm and click **Confirm**. Enable **Activate orchestration template**. 
    -  Under **Configurations** set following values:
        -  **Temperature:** `0`
        -  **Top P:** `0`
        -  **Top K:** `0` 
        -  **Max completion length:** `4096`

![add kb](/static/module2images/o1.png) 

![add kb](/static/module2images/o2.png) 

![add kb](/static/module2images/bsp51.png)

![add kb](/static/module2images/nfta1.png)

  - Click **KB response generation** enable **Override knowledge base response generation template defaults**.
::alert[Make sure Activate Knowledge Base response generation template is **disabled**] 
It will ask to confirm and click **Confirm**. 
   -  Under **Configurations** set following values:
      -  **Temperature:** `0`
      -  **Top P:** `0`
      -  **Top K:** `0`  

![add kb](/static/module2images/nfta151.png) 

![add kb](/static/module2images/k1.png) 

![add kb](/static/module2images/nfta66.png) 

![add kb](/static/module2images/bsp52.png) 

  - Click **Post-processing** enable **Override post-processing template defaults**. It will ask to confirm and click **Confirm**. Enable **Activate post-processing template**. 
     -  Under **Configurations** set following values:
        -  **Temperature:** `0`
        -  **Top P:** `0`
        -  **Top K:** `0` 
        -  **Max completion length:** `4096`

![add kb](/static/module2images/nfta152.png) 

![add kb](/static/module2images/pp1.png) 

![add kb](/static/module2images/bsp54.png) 

![add kb](/static/module2images/bsp55.png) 

19. At the bottom right corner **Save and exit**. 

20. In the agent console, scroll up and **Save and Exit**. After **Save and Exit**, scroll-up to read the message in the green banner. It is asking to prepare the agent **Agent: network_fault_troubleshooting_agent was successfully updated. Prepare the agent to keep its detail up to date**. 

![add kb](/static/module2images/tsse1.png)

- On the right side of the console under **Test** you will see **Prepare**. Click **Prepare**. Then you will read one more message in green banner which will say **Agent: network_fault_troubleshooting_agent was successfully prepared** (follow the red arrows and red boxes in below pictures). 

![add kb](/static/module2images/p1.png)
![add kb](/static/module2images/p2.png)

21. Click **Create Alias**. Set following values: 
    - **Alias name:** :code[networkfta]{showCopyAction=true} 
    - **description:** :code[agent alias]{showCopyAction=true}
- Click **Create Alias** at the bottom (follow the red arrows and red boxes in below pictures). 

![add kb](/static/module2images/nfta153.png)
![add kb](/static/module2images/nfta154.png)
![add kb](/static/module2images/ca3.png)

###### Note: We have not enabled Bedrock Guardrails but it is highly recommended to enable it and use other best practices when deploying it in production.  
### Congratulations! You have successfully created the agent. Move to Section4 to test the agent. 