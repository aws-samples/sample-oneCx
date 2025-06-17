---
title : " Run the billshock test case "
weight : 70
---

## You will be running below scenario. Before starting this section make sure all previous steps are completed successfully
###### Scenario1: Imagine you are a CSP providing Wireless services to your customer across the world. You have deployed this bill shock agent to address customer question's related to high bill. One of your customers is shocked to see the last month bill and asked for explanation.  
1. On the right side of the console, locate the chat window at the bottom (follow the red arrow in below picture). Copy and paste :code[why my bill is high]{showCopyAction=true} and hit enter. The agent responds with a greeting message and ask for `customer mobile number and secret key` for authentication (read the text in below picture). 

![add kb](/static/module2images/t1.png)

![add kb](/static/module2images/bs1.png)

2. Copy and paste :code[9000000002 435602]{showCopyAction=true} and hit enter. First the agent authenticates the user by checking customer mobile number and secret key. Then it calls the bill shock API to analyse the customer last month bill. It educates the customer why last month bill is high as compared to previous month. Also it explains the reasoning for high bill - customer used more roaming data and made more calls duing roaming. This led to increased bill. It suggest the customer to buy roaming plan called  Globetrotter Lite and explain the plan. Additionally it suggest the customer to disable the data roaming to provent accidental charges (read the text in below picture). 


![add kb](/static/module2images/bs60.png)

4. Copy and paste :code[How to disable it]{showCopyAction=true} and hit enter. Then it asks the customer to provide phone type - iphone or Android. Copy and paste :code[iphone]{showCopyAction=true} and hit enter. Agent provides the steps to disable data roaming (read the text in below picture).

![add kb](/static/module2images/bsp61.png)
![add kb](/static/module2images/bsp62.png)

5. Copy and paste :code[okie]{showCopyAction=true} and hit enter. Agent summarises the overall response (read the text in below picture). 

![add kb](/static/module2images/bsp63.png)

###### Now let's understand how agent found the root cause (For each agent's response click the associated **Show Trace**)
1. First agent identifies the customer mobile number and secret key from the customer response. Then it successfully authenticates the customer. It has full flexibility to make authentication more robust like 2 factor authentication. Sending OTP on registered mobile number or email and entering  those details in the chat. Then agent develops Chain of Thought to provide response to customer query. It analyses and compare last two months customer bill by calling bill API. It concludes that customer bill is high because of a) high data usage while roaming b) calls made during roaming. 
2. Then it checks **billshock-dataroamingplan-kb** knowledge base to find the suitable roaming plan for the customer.It suggest the customer to buy roaming plan. Then it checks **billshock-disabledataroaming-kb** knowledge base to help the customer to disable the data roaming to avoid accidental roaming charges. For each agent response click the associated **Show Trace** to understand the agent's Chain of Thought. You can integrate it with you broader product catalog. 

## Congratulations! You have successfully completed Bill Shock agent sub-module. 