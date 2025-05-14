---
title : " Data Load "
weight : 90
---
## Section1
###### In this section you will create Amazon RDS (MySQL) tables. Then you will load the customer authentication data, broadband plans for each customer, bill payment details, modem status and node status details into respective RDS tables. AWS Step Functions is used to orchestrate the data load related tasks. 

1. Inside AWS Console Search Bar (at the top of AWS Console) type **Step functions**. And under **Services** click to open it (see the red arrows in below picture). 

![Step Functions](/static/module2images/bsp91.png)

2. In Step Functions Console, select and click **ccj-techsupport-orchestration** (follow the red arrow in below picture). 

![ccj-techsupport-orchestration](/static/module2images/ccj-techsupport-orchestration.png)

3. In the right upper corner, click **Start Execution** (follow the red arrow in below picture). 

![Start Execution](/static/module2images/startexecution.png)

4. A new window will pop-up. Keep everything as default and click **Start execution** at the right bottom corner (follow the red arrow in below picture). 

![Start Execution](/static/module2images/startexecutionwindow.png)

5. A new window will appear and scroll down to the **Graph View**. Each State (example - CheckRDSAvailability) will execute one by one. After successful execution it will turn green and then it will move to the next state execution. All green means it has successfully executed (follow the red arrows in below picture).

![Successful Execution](/static/module2images/nfta75.png)

6. Congratulation! You have successfully loaded the data. 

### Congratulations! You have completed this section. Now move to the step2. 