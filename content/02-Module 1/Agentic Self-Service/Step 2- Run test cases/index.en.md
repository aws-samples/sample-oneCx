---
title : " Welcome to Agentic Self-Service "
weight : 150
---
## You will login to chat interface, run the test scenarios and architecture deep dive. 

1. In the AWS Console Search Bar type **Cloudformation** and under **Services** click **CloudFormation**. Under **Stack** select **frontend**. Then click **Outputs** and scroll to the bottom to copy **UiUsername** value and **UiPassword** value. Then click on **ReactAppApiEndpointE80AD34C** (last few strings may vary) value. A new webpage will open (follow the red arrows in below pictures). 

![Step Functions](/static/module2images/nfta28.png)
![Step Functions](/static/module2images/nfta29.png)
![Step Functions](/static/module2images/nfta30.png)
![Step Functions](/static/module2images/nfta30.png)

2. Click **SignIn**. Enter **UiUsername** value and ****UiPassword** value. And click **Sign In** (follow the red arrows in below pictures). 

![Step Functions](/static/module2images/nfta31.png)
![Step Functions](/static/module2images/nfta32.png)
![Step Functions](/static/module2images/nfta33.png)

3. A new webpage will open. Click **Agentic Self-Service** (follow the red arrow in below picture). 

![Step Functions](/static/module2images/nfta34.png)

###### Now you are ready to run test cases 

1. Imagine you are a tier-1 CSP with mobile and wirelines sevrices in B2C domain. You have a agentic customer chat self service where customers can ask mobile bill related querries and can get fixed line technical support. 
2.  Imagine one of your fixed line customer asks `why my network is down`.It will ask for **10-digit customer ID and 6-digit secret key**. Please enter **2000000002 357893**. It will provide a similar explanation that `The reason your network is down is because the node serving your area is currently not operational. Your modem appears to be functioning properly, but without an active node, you will not have internet connectivity. Unfortunately, there is no troubleshooting required from your side for this issue. Oktank's technical team is aware of the node failure and is working to restore services as soon as possible. Please bear with us as node outages can take some time to resolve. I will keep you updated once the node is back online and your network services are restored. Thank you for your patience and understanding.`

![Step Functions](/static/module2images/nfta35.png)

3. Now imagine there is an another customer (has mobile plan) asking another type of question like `why my bill is high`. It will ask **10-digit mobile number and 6-digit secret key**. Enter **9000000002 435602**. Then it might ask which type of mobile phone you have. Then enter **iphone**. Then it provides explaination why the bill is high because of data usage and calls during roaming. It also suggest to buy a roaming pack to manage roaming cost. Lastly it suggest to disable roaming while going abroad. 

![Step Functions](/static/module2images/nfta36.png)
![Step Functions](/static/module2images/nfta37.png)

###### Now let's understand how it works

1. Let's understand how this agentic chat service is working. Remember you created 2 Bedrock Agents a) Bill Shock Agent which analyses customer's mobile bills and help them understand why their bill is high and how it can help them to manage the cost. b) Wireline Network (or fixed network) Technical Support Agent which helps wireline customers to troubleshoot their network problems. So as an operator you have 2 types of customers like a) Mobile b) Wireline. 
2. Below is the high level Agentic Self-Service deployment architecture. When your customers ask a question through our intuitive chat interface, it invokes an Amazon API Gateway (As of Workshop studio limitation the request invokes an AWS Lambda URL directly. It is a best practice to invoke Lambda via API Gateway). At the heart of this Agentic Self-Service is the Multi-Agent Orchestrator.The Multi-Agent Orchestrator serves as a robust tool for implementing complex AI ecosystems that integrate various specialized agents. It is deployed on Lambda. 

![Step Functions](/static/module2images/mao1.png)
    
3. Now imagine you have deployed this Agentic Self-Service which will serve both type customers. How your chat service will identify the customer intent and select the appropriate Agent to process the request? Lets take a deeper look at Multi-Agent Orchestrator and understand how it works. Below is the Multi-Agent Orchestrator flow. 

![Step Functions](/static/module2images/mao2.png)

- (1). Request: The customer asks a query, lets assume it related to network fault. 
- (2). Orchestrator Invocation and Classification: Multi-Agent Orchestrator receives the query. Bedrock Classifier uses a LLM to analyse the request, agent description for the current user ID and session ID. This classifier determines the most appropriate agent for a) A new query b) A follow-up query. 
- (3). Agent Selection: The Classifier responds with name of the selected agent. In this case it will be Network Fault Troubleshoot agent.
- (4). Route to Agent: Multi-Agent Orchestrator routes the customer request to selected agent.
- (5). Agent Processing: Selected agent processes the user request. 
- (6). Reponse Generation: The agent generates a response and send it to Multi-Agent Orchetrator. 
- (7). Response Delivery: Multi-Agent Orchetrator sends the generated response back to the customer. 
4. Please visit the following link to know more about Multi-Agent Orchestrator -https://awslabs.github.io/multi-agent-orchestrator/ 

## Congratulations! You have successfully completed Agentic Self-Service sub-module. And you have also completed module 2- Customer support using agentic workflows