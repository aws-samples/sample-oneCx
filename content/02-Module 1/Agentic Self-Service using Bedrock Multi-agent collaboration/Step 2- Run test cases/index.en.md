---
title : " Welcome to Agentic Self-Service using Amazon Bedrock Multi-agent collaborator"
weight : 160
---

###### Now you are ready to run test cases 

1. Imagine you are a tier-1 CSP with mobile and wirelines sevrices in B2C domain. You have a agentic customer chat self service where customers can ask mobile bill related querries and can get fixed line technical support. 
2. On the right side of the console, locate the chat window at the bottom (follow the red arrows in below picture). 
  ![create agent](/static/module2images/mac15.png)

3.  Imagine one of your fixed line customer asks :code[why my network is down]{showCopyAction=true}. It will ask for **10-digit customer ID and 6-digit secret key**. Please enter :code[2000000002 357893]{showCopyAction=true}. It will provide a similar explanation that `The reason your network is down is because the node serving your area is currently not operational. Your modem appears to be functioning properly, but without an active node, you will not have internet connectivity. Unfortunately, there is no troubleshooting required from your side for this issue. Oktank's technical team is aware of the node failure and is working to restore services as soon as possible. Please bear with us as node outages can take some time to resolve. I will keep you updated once the node is back online and your network services are restored. Thank you for your patience and understanding.`

![Step Functions](/static/module2images/mac16.png)
![Step Functions](/static/module2images/mac17.png)

3. Now imagine there is an another customer (has mobile plan) asking another type of question like :code[why my bill is high]{showCopyAction=true}. It will ask **10-digit mobile number and 6-digit secret key**. Enter :code[9000000002 435602]{showCopyAction=true}. Then it might ask which type of mobile phone you have. Then copy and paste :code[iphone]{showCopyAction=true}. Then it provides explaination why the bill is high because of data usage and calls during roaming. It also suggest to buy a roaming pack to manage roaming cost. Lastly it suggest to disable roaming while going abroad. 

![Step Functions](/static/module2images/mac18.png)
![Step Functions](/static/module2images/mac19.png)

###### Now let's understand how it works

1. Let's understand how this agentic chat service is working. Remember you created 2 Bedrock Agents a) Bill Shock Agent which analyses customer's mobile bills and help them understand why their bill is high and how it can help them to manage the cost. b) Wireline Network (or fixed network) Technical Support Agent which helps wireline customers to troubleshoot their network problems. So as an operator you have 2 types of customers like a) Mobile b) Wireline. 
2. Below is the high level Agentic Self-Service deployment architecture. When your customers ask a question through Amazon Bedrock Multi-agent collaborator chat interface, it invokes the collaborating agent based on the customer intent. The Multi-Agent Orchestrator serves as a robust tool for implementing complex AI ecosystems that integrate various specialized agents. It is a managed agent. 

![Step Functions](/static/module2images/mac20.png)
    
3. Now imagine you have deployed this Agentic Self-Service which will serve both type customers. How your chat service will identify the customer intent and select the appropriate Agent to process the request? Lets take a deeper look at Multi-Agent Orchestrator and understand how it works. Below is the Multi-Agent Orchestrator flow. 

![Step Functions](/static/module2images/mac21.png)

- (1). Request: The customer asks a query, lets assume it related to network fault. 
- (2). Orchestrator Invocation: Bedrock Multi-Agent Collaboration agent receives the query. In Supervisor mode, the supervisor agent analyzes the input. Based on the customer intent, it then invokes the right subagent.  In this case it invokes **Network Fault Troublshooting agent**. After receiving responses from subagent, the supervisor agent processes them to determine if the problem is solved or if further action is needed. 
- (3). Agent Query Execution: Network Fault Troublshooting agent executes the customer query.
- (4). Route to Multi-agent Collaboration Agent: Network Fault Troublshooting agent sends the response to Multi-agent Collaboration Agent. 
- (5). Response Delivery: Multi-agent Collaboration Agent sends the generated response back to the customer. 
4. Please visit the following link to know more about Multi-Agent Orchestrator - https://aws.amazon.com/blogs/aws/introducing-multi-agent-collaboration-capability-for-amazon-bedrock/ 

## Congratulations! You have successfully completed Agentic Self-Service using Bedrock Multi-agent collaboration sub-module. And you have also completed module 2- Customer support using agentic workflows