---
title : " Amazon Bedrock Knowledge Base creation "
weight : 100
---
## Section 1 You will create the first Amazon Bedrock Knowledge Base **billpayment-kb**

1. In the AWS Console Search Bar (at the top of AWS Console), type **Bedrock** and then click **Amazon Bedrock** (follow the red arrow in below picture).

![Amazon Bedrock](/static/module2images/br.png)

2. On the left side bar of Bedrock Console, under **Builder tools** click **Knowledge bases** (follow the red arrow in below picture). 

![Knowledge base](/static/module2images/kb.png)

3. Click **create knowledge base** (follow the red arrow in below picture).

![create knowledge base](/static/module2images/createkb.png)

4. Set following values:
   - **Knowledge base name:** :code[billpayment-kb]{showCopyAction=true}
   - **Knowledge base description:** :code[knowledge base for helping customers to pay their broadband bill on different devices]{showCopyAction=true}
   - Keep IAM permissions for Runtime role as **Create and use a new service role** (follow the red arrows in below picture). 

![create knowledge base](/static/module2images/kb1.png)

5. Under **Choose data source** select **Amazon S3** and then click **Next** (follow the red arrows in below picture).

![create knowledge base](/static/module2images/bsp12.png)

6. Set following values:
   - **Data source:** :code[amazons3]{showCopyAction=true} 
   - Keep **data source location** as `This AWS account` 
   - Under **S3 URI** select **Browse S3**. Select the bucket with starting with :code[techsupport]{showCopyAction=true}. For example  `techsupport-347964218045-us-west-2-a453` (**note:** bucket name after **techsupport** will be different for each of you as bucket name has to be globally unique across AWS). Click **Choose** (follow the red arrows in below picture).

![create knowledge base](/static/module2images/bsp32.png)
![create knowledge base](/static/module2images/nfta71.png)

7. Under **Chunking and parsing configurations** select **custom**. Under **Chunking strategy** select **No chunking**. Keep other options as default and click **Next** (follow the red arrows in below pictures).

![create knowledge base](/static/module2images/chunk.png)

8. Under **Embeddings model** select **Titan Text Embeddings v2**. Under **Vector database** select **Quick create a new vector store - Recommended** and then click **Next** (follow the red arrow in below pictures).

![create knowledge base](/static/module2images/embed.png)

9. Note: Before you start this instruction do not leave this page after you click **Create knowledge base**. 
 - Firstly, review all the options a) Knowledge base name and description b) Data source and bucket name (S3 URI) c) Chunking Strategy d) Embeddings model e) Vector Store.

![create knowledge base](/static/module2images/nfta120.png)
![create knowledge base](/static/module2images/nfta121.png)

 - Secondly, if all looks fine then scroll to the bottom, click **Create knowledge base**. And scroll up to see the blue notification **Preparing vector database in Amazon Opensearch Serverless. This process may take several minutes to complete**. After a minute (in some  cases it takes a bit longer), blue notification turns green with the message **Amazon Opensearch Serverless vector database is ready.**

![create knowledge base](/static/module2images/aoss.png)
![knowledge base is ready](/static/module2images/aossready.png)

 - Then, automatically a new window is opened (please wait until a new window automatically opens) with following message on the top **Knowledge base 'billpayment-kb' is created successfully. Sync one or more data sources to index your content for searching.**
 
![Go to data source](/static/module2images/nfta72.png)

10. Click **Go to data sources** in the green notification on the top. Under **Data Source**,  select **amazons3** and click **Sync**. It will take few seconds to complete. You will get a green notification on the top **Sync completed for data source** (follow the red arrows and boxes in below pictures). 

![Go to data source](/static/module2images/nfta72.png)
![Sync](/static/module2images/sync.png)
![Sync complete](/static/module2images/syncomp.png)

11. Congratulations! This knowledge base is ready to use.

## Section 2 You will create the second and the last Amazon Bedrock Knowledge Base **modemtroubleshoot-kb**

1. On the left side bar of Bedrock Console, under **Builder tools** click **Knowledge bases** (follow the red arrow in below picture).

![Knowledge base](/static/module2images/kb.png)

2. Click **create knowledge base** (follow the red arrow in below picture). 

![create knowledge base](/static/module2images/createkb.png)

3. Set following values:
   - **Knowledge base name:** :code[modemtroubleshoot-kb]{showCopyAction=true}
   - **Knowledge base description:** :code[knowledge base for helping customers to troubleshoot their modem]{showCopyAction=true}
   - Keep IAM permissions for Runtime role as **Create and use a new service role** (follow the red arrows in below picture). 

![create knowledge base](/static/module2images/mkb.png)

4. Under **Choose data source** select **Amazon S3** and then click **Next** (follow the red arrows in below picture).

![create knowledge base](/static/module2images/bsp12.png)

5. Set following values:
   - **Data source:** :code[amazons3]{showCopyAction=true}
   - Keep **data source location** as `This AWS account` 
   - Under **S3 URI** select **Browse S3**. Select the bucket with starting with :code[modemts]{showCopyAction=true}. For example  `modemts-347964218045-us-west-2-a453` (**note:** bucket name after **modemts** will be different for each of you as    bucket name has to be globally unique across AWS). Click **Choose** (follow the red arrows in below pictures).

![create knowledge base](/static/module2images/bsp32.png)
![create knowledge base](/static/module2images/nfta73.png)

6. Under **Chunking and parsing configurations** select **custom**. Under **Chunking strategy** select **No chunking**. Keep other options as default and click **Next** (follow the red arrows in below pictures).

![create knowledge base](/static/module2images/chunk.png)

7. Under **Embeddings model** select **Titan Text Embeddings v2**. Under **Vector database** select **Quick create a new vector store - Recommended** and then click **Next** (follow the red arrows in below pictures).

![create knowledge base](/static/module2images/embed.png)

8. Note: Before you start this instruction do not leave this page after you click **Create knowledge base**. 
 - Firstly, review all the options a) Knowledge base name and description b) Data source and bucket name (S3 URI) c) Chunking Strategy d) Embeddings model e) Vector Store.

![create knowledge base](/static/module2images/nfta150.png)
![create knowledge base](/static/module2images/nfta74.png)

 - Secondly, if all looks fine then scroll to the bottom, click **Create knowledge base** (on the right corner). And scroll up to see the blue notification **preparing vector database in Amazon Opensearch Serverless. This process may take several minutes to complete** . After a minute (in few cases it may take a bit longer), blue notification turns green with the message **Amazon Opensearch Serverless vector database is ready.**

![create knowledge base](/static/module2images/maoss.png)
![knowledge base is ready](/static/module2images/maossready.png)

 - Then, automatically a new window is opened (please wait until a new window automatically opens) with following message on the top **Knowledge base 'billpayment-kb' is created successfully. Sync one or more data sources to index your content for searching** (follow the red arrows and box in below pictures). 

![Go to data source](/static/module2images/mds.png)

9. Click **Go to data sources** in the green notification on the top. Under **Data Source**,  select **amazons3** and click **Sync**. It will take few seconds to complete. You will get a green notification on the top **Sync completed for data source** (follow the red arrows and boxes in below pictures). 

![Go to data source](/static/module2images/mds.png)
![Sync](/static/module2images/msync.png)
![Sync complete](/static/module2images/msyncomp.png)

10. Congratulations! This knowledge base is ready to use. 

### Congratulations! You have successfully created two knowledge bases. Now move to Step3