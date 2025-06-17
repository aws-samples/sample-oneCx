---
title : " Create Amazon Bedrock Multi-Agent collaboration agent "
weight : 150
---

## Section 1 In this section you create Amazon Bedrock Multi-Agent collaboration agent. 
1. On the left side bar of Bedrock console, under **Builder tools** click **Agents**. And then click **Create Agent** (follow the red arrows and red box in below pictures).

![Step Functions](/static/module2images/agent.png)


![create agent](/static/module2images/createagent.png)

2. A new window will open, set name as :code[multi-agent-collaborator]{showCopyAction=true} and leave description field empty. Click **Enable multi-agent collaboration**. And click **Create**. You will get a  message on the top that **Agent: multi-agent-collaborator was successfully created** (follow the red arrows in below pictures).

![create agent](/static/module2images/mac1.png)
![create agent](/static/module2images/mac2.png)

3. Under **Agent resource role**, click **Use an existing service role**(follow the red arrows in below picture). 
![create agent](/static/module2images/mac3.png)

4. Under **Select model** select **Claude 3 Sonnet v1**. Click **Apply**(follow the red arrows in below picture). 
![create agent](/static/module2images/mac4.png)

5. Under **Instructions for the Agent**, copy and paste the following agent instruction(follow the red arrows in below picture).

:::code{showCopyAction=true showLineNumbers=false language=json}
You are customer service agent who orchestrates between bill shock agent and network_fault_troubleshooting_agent to serve the customers 
::: 

![create agent](/static/module2images/mac5.png)

6. Scroll up to the top and click **Save**(follow the red arrow in below picture).
![create agent](/static/module2images/mac6.png)

7. Scroll down to the bottom and click **Edit** under **Multi-agent collaboration**(follow the red arrows in below picture).
![create agent](/static/module2images/mac7.png)

8. Under **Collaboration configuration**, select **Supervisor**(follow the red arrow in below picture).
![create agent](/static/module2images/mac8.png)

9. Under **Agent collaborator**, click the arrow head to expand it(follow the red arrow in below picture).
![create agent](/static/module2images/mac9.png)

10. Now we will add the 2 agents (**bill_shock_agent** and **network_fault_troubleshooting_agent** ) which you created earlier. 
11. Add **bill_shock_agent**(follow the red arrows in below picture).
    - Under **Collaborator agent** select **bill_shock_agent**. 
    - Under **Agent alias** select **billshock_alias**. 
    - Under **Collaborator name** copy and paste :code[billshockagent]{showCopyAction=true}
    - Under **Collaborator instruction** copy and paste
:::code{showCopyAction=true showLineNumbers=false language=json}
  Use this agent only when customer a) has bill analysis questions like high bill and explain why the bill is high compared to other months. b) Help the customer to disable roaming on mobile phones. c) Help them buy roaming data plans. 
::: 
  - Check **Enable conversation history sharing**
  - Click **Add collaborator**. Under **Agent collaborator**, click the arrow head to expand it. 
  ![create agent](/static/module2images/mac10.png)


12. Add **network_fault_troubleshooting_agent**(follow the red arrows in below picture).
    - Under **Collaborator agent** select **network_fault_troubleshooting_agent**. 
    - Under **Agent alias** select **networkfta**. 
    - Under **Collaborator name** copy and paste :code[networkfaulttroubleshootingagent]{showCopyAction=true}
    - Under **Collaborator instruction** copy and paste
:::code{showCopyAction=true showLineNumbers=false language=json}
  Use this agent when a) customers have broadband network issues like why my nextwork is slow or not working. b) How to pay broadband bill.  
::: 
- Check **Enable conversation history sharing**
  ![create agent](/static/module2images/mac11.png)

13. Scroll-up and click **Save and Exit**.You will see a message on the top **Secondary agents are updated**(follow the red arrows in below picture).

  ![create agent](/static/module2images/mac12.png)
14. On the right side of the Bedrock Console, click **Prepare**. You will get a message on the top **Agent: multi-agent-collaborator was successfully prepared**(follow the red arrows in below pictures).

  ![create agent](/static/module2images/mac13.png)
  ![create agent](/static/module2images/mac14.png)

### Congratulations! You have successfully created multi agent collaboration agent. Move to step2 to see it in action
