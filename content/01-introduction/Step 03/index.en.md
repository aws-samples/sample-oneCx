---
title : "Explore the lambda functions and the prompts used for interacting with Bedrock"
weight : 30
---

## Objective
Learn how to examine and understand the prompts used in Lambda functions for:
- Summarizing customer journeys
- Generating chat responses through Bedrock

## Step-by-Step Guide

1. Access Lambda Service
   - Open AWS Console
   - Use the search bar to find **"Lambda"**

![Lambda Search](/static/intro-module-images/tlc302-ep-1.png)

2. Explore Customer Journey Summary Function
   - Go to **"Functions"** section
   - Search **"GetCustomerJourneyToBedrock"** in the search bar.

![Customer Journey Function](/static/intro-module-images/tlc302-ep-2.png)

::alert[Any changes made to the prompt or code may result in unexpected behaviour, hence make changes cautiously]{header="CAUTION!" type="error"}

3. Review Summary Prompt
   - In the code section, locate `prompt_message = '''`
   - Examine the prompt content

![Summary Prompt](/static/intro-module-images/tlc302-ep-3.png)

4. Explore Chat Interface Function
   - Return to **"Functions"** section
   - Select **"GetCustomerJourneyChatResponseLambda"** function

![Chat Function](/static/intro-module-images/tlc302-ep-4.png)

5. Review Chat Prompt
   - Find `prompt_message = '''` in the code
   - Study the prompt and consider potential modifications to customize responses

![Chat Prompt](/static/intro-module-images/tlc302-ep-5.png)

## Next Steps
You have completed the Introduction module. Please proceed to the next module.






    


