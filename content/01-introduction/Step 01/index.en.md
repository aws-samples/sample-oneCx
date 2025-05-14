---
title: "Visualize and Summarize a Customer Journey"
weight: 10
---

## Objective
Learn how to view and analyze individual customer journeys using Amazon Bedrock. This module demonstrates how to build a customer journey map and extract meaningful insights from customer interactions.

## Customer Journey Flow
The diagram below shows how a customer query flows through multiple services to deliver insights:

![SummarizeJourneyFlow|500x300](/static/intro-module-images/tlc302-intro-summarise-journey.png)


## Steps


::alert[Ensure you have completed the Lab Prerequisites section and can access the AWS Console]{header="Prerequisites"}


### 1. Access the UI Credentials
1. Navigate to CloudFormation:
   - In the AWS Console search bar, type **"cloudformation"** and click it

   ![rcj1-1|250x150](/static/intro-module-images/tlc302-rcj-1-1.png)


2. Find the Frontend Stack:
   - Click **"Stacks"** and click the **"frontend"** stack
   ![rcj1-2|250x150](/static/intro-module-images/tlc302-rcj-1-2.png)


3. Get Access Details:
   - In the **"Outputs"** section, note down:
     - ReactAppEndpoint
     - UiUsername
     - UiPassword

   ![rcj1-3|250x150](/static/intro-module-images/tlc302-rcj-1-3.png)


### 2. Log into the Application
1. Open the ReactAppEndpoint URL in your browser
2. Enter the username and password from step 1

   ![rcj2-1|250x150](/static/intro-module-images/tlc302-rcj-2-1.png)


### 3. View Customer Journey
1. Click **"Customer Journey"** in the top left
2. Enter a customer ID between (1-50) in the search window and hit the Enter button on your keyboard

   ![rcj3-1|250x150](/static/intro-module-images/tlc302-rcj-3-1.png)


3. Review the journey events and summary

   ![rcj3-2|250x150](/static/intro-module-images/tlc302-rcj-3-2.png)


### 4. Analyze the Results
Consider these key points while reviewing the customer journeys:

- Examine the chronological sequence of events
- Note the different types of customer interactions
- Compare the AI-generated summary against the actual events
- Think about how this journey mapping could benefit your own customers