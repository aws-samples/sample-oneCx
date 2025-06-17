---
title : "Module 1 - Customer support using agentic workflows "
weight : 20
---

## Introduction

Customer self-service capabilities are currently limited in their ability to address complex issues. While basic tasks can often be handled through automated systems, more intricate problems remain beyond the scope of existing self-service solutions. Specifically, customers face challenges when attempting to navigate high bill charges or when trying to diagnose and resolve technical network faults independently. As GenerativeAI rapidly advances, it presents a prime opportunity to revolutionize customer support. Now CSPs can develop cutting-edge self-service centers that offer more sophisticated, intuitive, and effective solutions for customers. 

In this module you will build Agentic Self-Service with following specialised agents: 
1. Agentic Wireless Billshock Support  
2. Agentic Wireline Network Technical Support 

Also, you will learn how a **Multi-Agent Orchestrator** is able to orchestrate these specalised agents based on customer queries. Below is the high level architecture. 

![Step Functions](/static/module2images/mao1.png) 


::alert[Before you start]
1. Make sure you have the completed **Lab Prerequisites**. 
2. After you login into AWS Management Console (AWS Console) make sure you are in **Oregon/us-west-2** region (follow the red arrow in below picture). 

![AWS Console](/static/module2images/awsconsole.png)



:::alert{header="Important note"}
Agentic Wireline Network Technical Support and Agentic Wireless Billshock Support are independent sub-modules hence you can run them in any order. However Agentic Self-Service is dependent on Agentic Wireline Network Technical Support and Agentic Wireless Billshock Support so make sure you complete them before you start to build Agentic Self-Service. 
Most steps are accompanied by screen-shots to provide you some visual guidance in addition to the textual description. 
Have fun!
::: 
