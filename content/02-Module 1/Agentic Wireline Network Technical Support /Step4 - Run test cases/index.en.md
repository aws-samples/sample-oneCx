---
title : " Test the agent "
weight : 120
---

## You will test the agent in following three scenarios. Before running these test cases make sure you have completed all the previous steps successfully. 

###### Scenario1: Imagine you are a tier-1 broadband provider and you have deployed this agent to help your customers to troubleshoot network problems.One of your customers is experiencing slow upload and download speed.Let's use this agent to find out the root cause for this customer network slowness. 

1. On the right side of the console, under **Test** click the drop down and select **networkfta: Version 1**. Now locate the chat window at the bottom.  Type `hi` and press enter. Agent will respond with welcome message and ask to enter `customer ID and secret key` for authentication purpose (read the text in below picture). 

![add kb](/static/module2images/t0.png)
![add kb](/static/module2images/nfta51.png)

2. Paste following details in the chat **2000000006 357897** and hit enter. As you notice customer didn't provide the details like which of them is customer ID and secret key. It successfully authenticates the customer and then ask could you please tell me your network problem.Paste following query in chat window `why my network is slow today` and hit enter (read the text in below picture). 

![add kb](/static/module2images/nfta54.png)

3. The agent provides the explanation that the customer has not paid the last month bill and this is the reason why customer's network speed is throttled. Now agent is requesting the customer to pay the bill and offers to help with payment instructions. Type `yes`(read the text in below picture). 

![add kb](/static/module2images/nfta55.png)

4. It asks which device you use like Windows, Mac or Android or similar. Enter `Samsung` in the chat and hit enter. Then it asks the customer which Samsung device you use like smartphone, tablet or computer. Type `phone` and hit enter (read the text in below picture).

![add kb](/static/module2images/nfta56.png)

5. Agent provides steps to pay the bill and educates the customer that it may take 1hour to get the speed restored(read the text in below picture). Type `okie` and hit enter. And then type `paid`(read the text in below pictures). 

![add kb](/static/module2images/nfta57.png)

![add kb](/static/module2images/nfta58.png)


###### Now let's understand how agent found the root cause (For each agent response click the associated **Show Trace**)
1. First agent identified the customer ID and secret key from the customer response. And then agent performed the authentication by invoking the authentication API. In your case it could your customer database which holds customer authentication details. It has full flexibility to make authentication more robust like two-factor authentication. Sending OTP on registered mobile number or email and entering those details in the chat. 
2. After successful authentication it invoked speedstatus API to find the current speed of the customer and also invoked bill payment API to check whether customer has paid the bill or not. The agent concludes that this case customer has not paid the bill. We can also integrate this API with your Business Support Systems to verify whether customer has paid the bill or not. 
3. As a CSP (Communication Service Provider) you have set-up a rule that speed will be throttled for non-payment of monthly dues. 
4. Now to help the customer to pay the bill, Agent calls the knowledge base to pull the payment details. It concludes that Samsung makes smartphones, tablets and computers, hence it confirms the device type with the customer. Here we can make it more advance by sending the payment link in the chat or email the payment link.
5. Finally it educates the customer that speed will be restored within 1 hour. 
6. More functionalities can be added like send an SMS/EMAIL when speed is restored. 


###### Scenario2: Imagine you are a tier-1 broadband provider and you have deployed this agent to help your customers to troubleshoot network problems. One of your customers is experiencing network outage. Let's use this agent to find out the root cause for this customer network outage.
1. Do a console refresh to load the new chat window page. On the right side of the console, under **Test** click the drop down and select **networkfta: Version 1**. Now locate the chat window at the bottom.  Type `hi` and press enter. Agent will respond with welcome message and ask to enter `customer ID and secret key` for authentication purpose (read the text in below pictures). 

![add kb](/static/module2images/t0.png)
![add kb](/static/module2images/nfta51.png)

2. Paste following details in the chat **2000000008 357899** and hit enter. As you notice customer didn't provide the details like which of them is customer ID and secret key. It successfully authenticates the customer and then ask could you please tell me your network problem. Type `why my network is down` and hit enter (read the text in below picture).

![add kb](/static/module2images/nfta59.png)

3. The agent provides the explanation that customer's modem is down and this is the reason for network outage. Also agent found that customer has not paid the last month bill which leads to speed throttling. And then explains even if the modem will be up you will experinece slow speed. Then it helps the customer to troubleshoot the modem step by step. Type `Yes` in chat window and hit enter.  (read the text in below picture). 

![add kb](/static/module2images/nfta60.png)

4. Then it ask the customer to check the power supply and verify the cable connection (read the text in below picture). Type `looks fine` and hit enter. 

![add kb](/static/module2images/t8.png)

5. Then it suggests to reboot the modem(read the text in below picture). 

![add kb](/static/module2images/t9.png) 

6. Type `it works now`and hit enter.
7. Now agent educates the customer the network is back online but you will experience slow network. And request to make the payment. Then ask the customer whether he/she needs help with the payment(read the text in below picture). 

![add kb](/static/module2images/t10.png) 

8. Type `Yes` and hit enter
9. Agent asks the customer which device he/she is using currently 
10. Type `iphone` and hit enter. It provide the steps how to make the payment using iphone (read the text in below picture). 

![add kb](/static/module2images/nfta62.png) 

12. Type `paid the bill` and hit enter. Agent educates the customer that it may take upto 1 hour to restore the speed(read the text in below picture). 

![add kb](/static/module2images/nfta63.png) 


###### Now let's understand how agent found the root cause (For each agent response click the associated **Show Trace**)
1. First agent identified the customer ID and secret key from the customer response. And then agent performed the authentication by invoking the authentication API. In your case it could your customer database which holds customer authentication details. It has full flexibility to make authentication more robust like 2 factor authentication. Sending OTP on registered mobile number or email and entering  those details in the chat.
2. It invokes modem status API to check whether modem is up or not. Then it chcalls the bill status API to check whether customer has paid the bill or not. In this case customer's modem is down which is the root cause. Also agent found that customer has not paid the bill which will cause an additional network issue. So the agent proactively informs the customer and saves you (as CSP) another customer touchpoint thereby saving dollars. 
3. Then Agent uses modem troubleshoot knowledge base to troubleshoot the modem. Here we can integrate with multi-modal to provide images as part of troubleshooting steps. 
4. Similarly Agent uses bill payment knowledge base to help the customer pay the bill. Here we can make it more advance by sending the payment link in the chat or email the payment link on the fly. 
5. More functionalities can be added like send an SMS/EMAIL when speed is restored. 

###### Scenario3: Imagine you are a tier-1 broadband provider and you have deployed this agent to help your customers to troubleshoot network problems. One of your customers is experiencing network outage. Let's use this agent to find out the root cause for this customer network slowness. 
1. Do a console refresh to load the new chat window page. On the right side of the console, under **Test** click the drop down and select **networkfta: Version 1**. Now locate the chat window at the bottom.  Type `hi` and press enter. Agent will respond with welcome message and ask to enter `customer ID and secret key` for authentication purpose (read the text in below pictures). 

![add kb](/static/module2images/t0.png)
![add kb](/static/module2images/nfta51.png)

2. Paste following details in the chat **2000000002 357893** and hit enter. Do a console refresh to load the new chat window page. On the right side of the console, locate the chat window at the bottom. Type `why my network is down` and the agent responds with a greeting message and ask for `customer ID and secret key` for authentication(read the text in below picture). 

![add kb](/static/module2images/t11.png)

3. Copy and paste following details in the chat **2000000002 357893**. As you notice customer didn't provide the details like which of them is customer ID and secret key. It successfully authenticates the customer and then ask could you please tell me your network problem. Type `why my network is down` and hit enter (read the text in below picture).

![add kb](/static/module2images/nfta64.png)

4. Agent found the node connecting to the customer modem is down. It educates the customer we are working to fix the issue(read the text in below picture). 

![add kb](/static/module2images/t12.png)

###### Now let's understand how agent found the root cause (For each agent response click the associated **Show Trace**)
1. First agent identified the customer ID and secret key from the customer response. And then agent performed the authentication by invoking the authentication API. In your case it could your customer database which holds customer authentication details. It has full flexibility to make authentication more robust like 2 factor authentication. Sending OTP on registered mobile number or email and entering  those details in the chat.
2. Then it locates customer modem details then find the corresponding node details. All these informations are stored in different tables. Once it is able to locate the related node then it invokes the node status API to check its status. It concludes that this node is down. In real world use case we can integrate it with node health check monitoring system. 

## Congratulations! You have completed  Agentic Wireline Network Technical Troubleshooting sub-module.   
