---
title : "Lab Prerequisites"
weight : 01
---

## Important note:
1. This workshop requires following skills 
   - Level 100 AWS Cloud skills 
   - Level 100 GenerativeAI knowledge (terms like prompts, intent, agents, LLM etc) 
   - Level 100 scripting knowledge 
2. This workshop can only run in AWS account provisioned by Workshop Studio. 
3. Baseline AWS Services are deployed in AWS Oregon (us-west-2) region. Hence use this region for building the modules. 

## Section 1
###### Log in with AWS Workshop Portal
1. If you are part of a hosted AWS event, the Workshop Studio Portal will be used. [Click here](https://catalog.us-east-1.prod.workshops.aws/join)  to join. Then click the Email One-Time Password (OTP) button.

![Amazon Bedrock](/static/prereqimages/pr1.png)

2. Enter your own email account and click the Send passcode button.

![Amazon Bedrock](/static/prereqimages/pr2.png)

3. In the email inbox, check the subject Your one-time passcode email and copy the passcode. Paste the copied passcode, then press the Sign in button.

![Amazon Bedrock](/static/prereqimages/pr3.png)

4. When you get to the Event Access code screen - enter the 12-digit Event Access code code you received from the event organizer. Click the Next Button to proceed.

![Amazon Bedrock](/static/prereqimages/pr4.png)

5. On the next screen, check the Accept Terms & Conditions box. Click the Join event button to proceed to the next step.

![Amazon Bedrock](/static/prereqimages/pr6.png)

6. Please note module instructions are on the left side of the console. 
7. To login to AWS Management Console (AWS Console), click **Open AWS Console** located on the left hand side of the screen to access the AWS Management Console page. Please make sure you are in the **Oregon, us-west-2** region. 

![Amazon Bedrock](/static/prereqimages/oaws.png)
    
7. Once you've followed all of the above steps, you are ready to start building the modules!


## Section 2
###### Enable Amazon Bedrock Models
1. Type Bedrock on the AWS Management Console Search bar and click to open the service (follow the red arrows in below picture).

![Amazon Bedrock](/static/module2images/br.png)

2. On the right side of Amazon Bedrock Console click **Get Started** (follow the red arrow in below picture).

![Amazon Bedrock Get Started](/static/module2images/brgetstarted.png)

3. On the left side bar of the Amazon Bedrock Console, scroll down to **Bedrock configuration**. Click **Model access** (follow the red arrow in below picture).

![Model access](/static/module2images/modelaccess1.png)

4. Click **Enable specific models**. Under **Amazon** select **Titan Text Embeddings V2** model and under **Anthropic** select **Claude 3 Sonnet** and **Claude 3 Haiku** models. Click **Next** at the left bottom corner (follow the red arrow in below pictures). 

![Enable specific models](/static/module2images/enablespecificmodels1.png)
![Select Amazon and Anthropic Models](/static/module2images/amazonandathropicmodel.png)
![Next](/static/module2images/modelnext.png)

5. Click **Submit** (follow the red arrow in below picture)

![Submit](/static/module2images/brsubmit.png)

6. Amazon Titan Text Embeddings V2 model will be enabled instantly. Anthropic Claude 3 Sonnet and Claude 3 Haiku will take upto a minute. Please refresh the page to see the updated model access. All three models are enabled (follow the red arrows in below picture).  

![Access Granted](/static/module2images/models1.png)

7. Do not proceed with next step until you have enabled all three models. 
8. Congratulations! You have successfully enabled the models. 

### Congratulations! You have successfully completed the pre-requisites. 
