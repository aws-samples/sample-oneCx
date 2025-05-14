---
title : " Billshock Data Load "
weight : 40
---

## Section1
###### In this section you will create Amazon RDS (MySQL) tables. Then you will load the customer authentication data (synthetic data) into Amazon DynamoDB table. And then you will load customer billing and usage details like roaming data and associated charges, roaming call duration and associated charges and other customer details into RDS tables. AWS Step Functions is used to orchestrate the data load related tasks. 

1. Inside AWS Console Search Bar (at the top of AWS Console) type **Step functions**. And under **Services** click to open it (see the red arrows in below picture). 

![Step Functions](/static/module2images/bsp91.png)

2. In Step Functions Console, select and click **ccj-billshock-orchestration** (follow the red arrow in below picture). 

![ccj-techsupport-orchestration](/static/module2images/bsp92.png)

3. In the right upper corner, please click **Start Execution** (follow the red arrow in below picture). 

![Start Execution](/static/module2images/se.png)
    
4. A new window will pop-up. Keep everything as default and click **Start execution** at the right bottom corner (follow the red arrow in below picture).

![Start Execution](/static/module2images/startexecutionwindow.png)

5. A new window will appear and then scroll down to the **Graph View**. Each State (example - **CheckRDSAvailability**) will execute one by one. After successful execution it will turn green and then it will move to the next state execution. All green means it has successfully executed (follow the red arrows in below picture).

![Successful Execution](/static/module2images/successfulexecution.png)

6. Congratulations! You have successfully loaded the data. 

### Congratulations! You have completed this section. Now move to the step2. 