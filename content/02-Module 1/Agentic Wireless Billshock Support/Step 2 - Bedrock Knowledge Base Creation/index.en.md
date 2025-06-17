---
title : " Amazon Bedrock Knowledge Base creation "
weight : 50
---
## Section 1 You will create first Amazon Bedrock Knowledge Base **billshock-disabledataroaming-kb**

1. In the AWS Console Search Bar (at the top of AWS Console), type **Bedrock** and then click **Amazon Bedrock** (follow the red arrows in below picture).

![Amazon Bedrock](/static/module2images/br.png)

2. On the left side bar of Bedrock Console, under **Builder tools** click **Knowledge bases** (follow the red arrow in below picture).

![Knowledge base](/static/module2images/kb.png)

3. Click **create knowledge base** (follow the red arrow in below picture).

![create knowledge base](/static/module2images/createkb.png)


4. Set following values: 
   - **Knowledge base name:** :code[billshock-disabledataroaming-kb]{showCopyAction=true}
   - **Knowledge base description:** :code[knowledge base for disabling data roaming on iphone]{showCopyAction=true}
   - Keep **IAM permissions** for Runtime role as **Create and use a new service role** (follow the red arrows in below picture). 

![create knowledge base](/static/module2images/bsp11.png)

5. Under **Choose data source** select **Amazon S3** and then click **Next** (follow the red arrows in below picture).

![create knowledge base](/static/module2images/bsp12.png)

6. Set following values:
   - **Data source:** :code[amazons3]{showCopyAction=true}
   - Keep **data source location** as `This AWS account`
   - Under **S3 URI** select **Browse S3**. Select the bucket with starting with :code[disableroaming]{showCopyAction=true}. For example `disableroaming-347964218045-us-west-2-a453` (**note:** bucket name after **disableroaming** will be different for each of you as bucket name has to be globally unique across AWS). Click **Choose** (follow the red arrows in below pictures).

![create knowledge base](/static/module2images/bsp13.png)
![create knowledge base](/static/module2images/bsp67.png)
![create knowledge base](/static/module2images/bsp68.png)

7. Under **Chunking and parsing configurations** select **custom**. Under **Chunking strategy** select **No chunking**. Keep other options as default and click **Next** (follow the red arrows in below pictures).

![create knowledge base](/static/module2images/chunk.png)

8. Under **Embeddings model** select **Titan Text Embeddings v2**. Under **Vector database** select **Quick create a new vector store - Recommended** and then click **Next** (follow the red arrows in below pictures).

![create knowledge base](/static/module2images/embed.png)



9. Note: Before you start with this instruction do not leave this page after you click **Create knowledge base** (follow the respective red arrows and boxes in below pictures). 
 - Firstly, review all the options a) Knowledge base name and description b) Data source and bucket name (S3 URI) c) Chunking Strategy d) Embeddings model e) Vector Store. 

![create knowledge base](/static/module2images/bsp15.png)
![create knowledge base](/static/module2images/bsp69.png)

 - Secondly, if all looks fine then scroll to the bottom, click **Create knowledge base**. And scroll up to see the blue notification **Preparing vector database in Amazon Opensearch Serverless. This process may take several minutes to complete** . After a minute (in some  cases it can take a bit longer), blue notification turns green with the message **Amazon Opensearch Serverless vector database is ready**. 

![create knowledge base](/static/module2images/bsp17.png)
![knowledge base is ready](/static/module2images/bsp18.png)

 - Then, automatically a new window is opened (please wait until a new window automatically opens) with following message on the top **Knowledge base 'billshock-disabledataroaming-kb' is created successfully. Sync one or more data sources to index your content for searching.** 

![Go to data source](/static/module2images/bsp19.png)

10. Click **Go to data sources** in the green notification on the top. Under **Data Source**, select **amazons3** and click **Sync**. It will take few seconds to complete. You will get a green notification on the top **Sync completed for data source** (follow the respective red arrows and boxes in below pictures). 

![Go to data source](/static/module2images/bsp19.png)
![Sync](/static/module2images/bsp20.png)
![Sync complete](/static/module2images/bsp21.png)

11. Congratulations! This knowledge base is ready to use.

## Section 2 You will create second and last Amazon Bedrock Knowledge Base - **billshock-dataroamingplan-kb**

1. On the left side bar of Bedrock Console, under **Builder tools** click **Knowledge bases** (follow the red arrow in below picture)

![Knowledge base](/static/module2images/kb.png)

2. Click **create knowledge base** (follow the red arrow in below picture). 

![create knowledge base](/static/module2images/createkb.png)

3. Set following values: 
   - **Knowledge base name:** :code[billshock-dataroamingplan-kb]{showCopyAction=true}
   - **Knowledge base description:** :code[knowledge base for all data roaming plans]{showCopyAction=true}
   - Keep **IAM permissions** for Runtime role as **Create and use a new service role** (follow the red arrows in below picture).

![create knowledge base](/static/module2images/bsp30.png)

4. Under **Choose data source** select **Amazon S3** and then click **Next** (follow the red arrow in below picture).

![create knowledge base](/static/module2images/bsp12.png)

5. Set following values:
   - **Data source:** :code[amazons3]{showCopyAction=true}
   - Keep **data source location** as `This AWS account`
   - Under **S3 URI** select **Browse S3**. Select the bucket with starting with :code[dataplans]{showCopyAction=true}. For example `dataplans-347964218045-us-west-2-a453` (**note:** bucket name after **dataplans** will be different for each of you as bucket name has to be globally unique across AWS). Click **Choose** (follow the red arrows in below pictures).

![create knowledge base](/static/module2images/bsp32.png)
![create knowledge base](/static/module2images/bsp71.png)

6. Under **Chunking and parsing configurations** select **custom**. Under **Chunking strategy** select **No chunking**. Keep other options as default and click **Next** (follow the red arrows in below pictures).

![create knowledge base](/static/module2images/chunk.png)

7. Under **Embeddings model** select **Titan Text Embeddings v2**. Under **Vector database** select **Quick create a new vector store - Recommended** and then click **Next** (follow the red arrows in below pictures).

![create knowledge base](/static/module2images/embed.png)

8. Note: Before you start this instruction do not leave this page after you click **Create knowledge base** (follow the respective red arrows and boxes in below pictures). 
 - Firstly, review all the options a) Knowledge base name and description b) Data source and bucket name (S3 URI) c) Chunking Strategy d) Embeddings model e) Vector Store. 

![create knowledge base](/static/module2images/bsp35.png)
![create knowledge base](/static/module2images/bsp72.png)

 - Secondly, if all looks fine then scroll to the bottom, click **Create knowledge base** (on the right corner). And scroll up to see the blue notification **preparing vector database in Amazon Opensearch Serverless. This process may take several minutes to complete** . After a minute (in few cases it may take a bit longer), blue notification turns green with the message **Amazon Opensearch Serverless vector database is ready**. 

![create knowledge base](/static/module2images/bsp37.png)
![knowledge base is ready](/static/module2images/bsp38.png)

 - Then, automatically a new window is opened (please wait until new window automatically opens) with following message on the top **Knowledge base 'billshock-dataroamingplan-kb' is created successfully. Sync one or more data sources to index your content for searching**. 

![Go to data source](/static/module2images/bsp39.png)

9. Click **Go to data sources** in the green notification on the top. Under **Data Source**,  select **amazons3** and click **Sync**. It will take few seconds to complete. You will get a green notification on the top **Sync completed for data source** (follow the respective red arrows and boxes in below pictures). 

![Go to data source](/static/module2images/bsp39.png)
![Sync](/static/module2images/bsp40.png)
![Sync complete](/static/module2images/bsp41.png)

10. Congratulations! This knowledge base is ready to use. 

### Congtratulations on completing Section 1 and Section 2. Now move to Step3