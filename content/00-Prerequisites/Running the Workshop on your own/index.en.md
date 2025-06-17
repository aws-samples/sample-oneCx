---
title: "Running the Workshop on your own"
weight: 03
---

## Prerequisites

### AWS Account Requirements
1. An AWS account with Administrator IAM Role access
2. Ensure you have access to the AWS Management Console

### Region Selection
- This solution must be deployed in US West (Oregon) region
- All resources will be created in the us-west-2 (Oregon) region

### VPC Considerations
- This solution will create 2 new VPCs as part of the deployment
- By default, AWS accounts have a limit of 5 VPCs per region
- Before deploying:
  - Check your current number of VPCs in the target region
  - If you already have more than 3 VPCs, consider either:
    - Deleting unused VPCs
    - Requesting a VPC limit increase from AWS Support
    - Choose a different account for deployment
  - To check existing VPCs:
    1. Navigate to the VPC Console
    2. Look for the "Your VPCs" section
    3. Count the number of existing VPCs

### Additional Requirements
- Ensure you have permissions to:
  - Create and manage IAM roles and policies
  - Create CloudFormation stacks
  - Create and manage VPC resources
  - Create and manage other AWS services used in this solution

> **Note:** If you don't have the required permissions or are unsure about your access levels, please contact your AWS account administrator.

### 1. S3 Bucket Setup
1. Navigate to Amazon S3 service page
2. Create a new bucket with a unique name:
   - Format: `agentic-workflow-assets-<your-account-number>`
3. Click on Enable under Bucket Versioning (This is important)
4. Make a note of the S3 bucket name for later use
5. Download and extract the [Assets.zip](https://ws-assets-prod-iad-r-pdx-f3b3f9f1a7d6a3d0.s3.us-west-2.amazonaws.com/12442fd8-5f6e-4ed7-96d7-56d590fe101e/assets.zip) File to your laptop

6. Upload all files to the newly created S3 bucket


### 2. Create CloudFormation Stack

The solution requires creating multiple CloudFormation stacks in a specific order. To orchestrate this, we leverage CodePipeline service to deploy these Stacks in sequenze:

   - Navigate to CloudFormation service page
   - Create a Stack using "self-deploy-codepipeline.json" template (part of the zip file downloaded earlier)
   - Stack name: `self-deploy` (or your preferred name)
   - S3BucketName: Enter the bucket name noted earlier
   - S3BucketPrefix: Leave blank
   - Leave other parameters unchanged
   - Click Next
   - Leave default parameters unchanged
   - Click Next
   - Review all settings
   - Check "I acknowledge that AWS CloudFormation might create IAM resources"
   - Check "I acknowledge that AWS CloudFormation might require the following capability: CAPABILITY_AUTO_EXPAND"
   - Click Next
   - Click Submit   
   - Wait for status: CREATE_COMPLETE

> **Note:** Please note, it takes more than an hour to deploy this solution. You can go to CodePipeline service and monitor the progress of Stack deployment. 

### Amazon Bedrock Model Access Setup

1. Access Amazon Bedrock
   - Open AWS Management Console
   - Search for "Bedrock"
   - Select Amazon Bedrock service
   ![Amazon Bedrock](/static/module2images/br.png)

2. Configure Model Access
   - Navigate to Model access under Bedrock configuration
   ![Model access](/static/module2images/modelaccess1.png)

3. Enable Required Models
   - Click "Enable specific models"
   - Under Amazon, select:
     - Titan Text Embeddings V2
   - Under Anthropic, select:
     - Claude 3 Sonnet
     - Claude 3 Haiku
   - Click Next
   ![Enable specific models](/static/module2images/enablespecificmodels2.png)
   ![Select Amazon and Anthropic Models](/static/module2images/amazonandathropicmodel.png)
   ![Next](/static/module2images/modelnext.png)

4. Complete Model Access Setup
   - Click Submit
   ![Submit](/static/module2images/brsubmit.png)

5. Verify Model Access
   - Amazon Titan Text Embeddings V2 will be enabled immediately
   - Anthropic Claude models may take up to a minute to enable
   - Refresh the page to see updated model access status
   ![Access Granted](/static/module2images/models1.png)

> **Important:** You can proceed with next steps while model enablement runs in the background. Return after a few minutes to verify successful model activation.

## Completion
Congratulations! You have successfully:
- Created the required S3 bucket
- Deployed the CloudFormation stack
- Enabled necessary Bedrock models

You are now ready to proceed with the workshop.
