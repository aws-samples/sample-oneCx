---
title : " Update Bedrock agent Id and Alias Id in paramter store "
weight : 140
---

## Section1 In this section you will update **network_fault_troubleshooting_agent** ID and **Alias ID** in SSM parameter store. 
1. In the AWS Console Search Bar, type Bedrock and select Amazon Bedrock. On the left side of the console under **Builder tools** click **Agents**. Then select **network_fault_troubleshooting_agent**. Under ** Agent overview**, make a note of **ID**. Scroll to the bottom of the page, under **Alias**, make a note of **Alias ID** (follow the red arrows in below pictures). 

![Step Functions](/static/module2images/nfta5.png)
![Step Functions](/static/module2images/nfta4.png)
![Step Functions](/static/module2images/nfta6.png)
![Step Functions](/static/module2images/nfta7.png)

2. In AWS Console Search Bar, type **SSM** and select **Systems Manager**. On the left side of the console, under **Application Management** click **Parameter Store**. Select **/Techsupport/agent_id** and click **Edit** and scroll to the bottom. Under **Value** please put value of **network_fault_troubleshooting_agent ID** and click **Save changes** (copied in step1)(follow the red arrows in below pictures).

![Step Functions](/static/module2images/nfta8.png)
![Step Functions](/static/module2images/nfta9.png)
![Step Functions](/static/module2images/nfta10.png)
![Step Functions](/static/module2images/nfta11.png)
![Step Functions](/static/module2images/nfta12.png)
![Step Functions](/static/module2images/nfta13.png)

3. Now Select **/Techsupport/agent_alias_id** and click **Edit** and scroll to the bottom. Under **Value** please put value of **network_fault_troubleshooting_agent Alias ID** (NOT agent ID) and click **Save changes** (copied in step1)(follow the red arrows in below pictures).

![Step Functions](/static/module2images/nfta14.png)
![Step Functions](/static/module2images/nfta15.png)
![Step Functions](/static/module2images/nfta16.png)

4. Please make sure you updated the right **Parameter store** values with **network_fault_troubleshooting_agent ID** and **network_fault_troubleshooting_agent Alias ID**. 

## Section2 In this section you will update **bill_shock_agent** ID and **Alias ID** in SSM parameter store. 

1. In the AWS Console Search Bar, type Bedrock and then click the Bedrock Service(follow the red arrows in below picture). 

![Amazon Bedrock](/static/module2images/br.png)

2. In the Amazon Bedrock Console, on the left side of the console under **Builder tools** click **Agents**. Then select **bill_shock_agent**. Under **Agent overview**, make a note of **ID**. Scroll to the bottom of the page, under **Alias**, make a note of **Alias ID**(follow the red arrows in below pictures). 

![Step Functions](/static/module2images/nfta17.png)
![Step Functions](/static/module2images/nfta18.png)
![Step Functions](/static/module2images/nfta19.png)

2. In AWS Console Search Bar, type **SSM** and select **Systems Manager**. On the left side of the console, under **Application Management** click **Parameter Store**. Select **/billshock/agent_id** and click **Edit** and scroll to the bottom. Under **Value** please put value of **bill_shock_agent ID** and click **Save changes** (copied in step1)(follow the red arrows in below pictures).

![Step Functions](/static/module2images/nfta8.png)
![Step Functions](/static/module2images/nfta9.png)
![Step Functions](/static/module2images/nfta20.png)
![Step Functions](/static/module2images/nfta21.png)
![Step Functions](/static/module2images/nfta22.png)
![Step Functions](/static/module2images/nfta23.png)

3. Now Select **/billshock/agent_alias_id** and click **Edit** and scroll to the bottom. Under **Value** please put value of **bill_shock_agent Alias ID** (NOT agent ID) and click **Save changes** (copied in step1)(follow the red arrows in below pictures).

![Step Functions](/static/module2images/nfta24.png)
![Step Functions](/static/module2images/nfta25.png)
![Step Functions](/static/module2images/nfta26.png)
![Step Functions](/static/module2images/nfta27.png)

4. Please make sure you updated the right **Parameter store** values with **bill_shock_agent ID** and **bill_shock_agent Alias ID**.  

### Congratulations! You have successfully updated the parameter store values. 
