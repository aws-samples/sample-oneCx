---
title : "Offer eligibility prompt, Customer segmentation and product recommendation agents"
weight : 10
---


::alert[This section will show you how the prompts and agents for offer eligibiliity check, customer segmentation, and product recommendation have been configured. We would recommend spending about 5min on this section. We will opensource the code soon after `re:Invent 2024` so that you can have a deeper look and reuse in your projects as appropriate.]

::expand[Answer: 42]{header="Question: What is the meaning of life?"}


## Explore the Customer Offer Eligibility checker prompt

Please work through the following steps in sequence:

**Step 1:** Access Amazon Bedrock

Open the Amazon Bedrock console by typing Bedrock in the AWS console search bar:

![Bedrock console](/static/Module3/images/bedrock-console.png)


---


**Step2:** Examine prompts for offer eligibility check.

a. Navigate to Prompt Management menu from the left hand panel and then click on **OfferEligibilityChecker**:

![Prompt Management](/static/Module3/images/bedrock-promptmgmt.png)


b. Scroll down and click on **Edit in prompt builder**

![edit prompt](/static/Module3/images/edit-promptv1.png)

c. You should see a prompt as follows:

Examine the prompt and its format. This prompt analyzes the customer journey to check if the events in the journey qualify the customer for an offer.The best part about this kind of solution is that the qualification criteria can be described in natural language. The LLM is able to analyze and determine whether the customer journey qualifies based on the described criteria.

Notice how the xml tags for context, objective, style_and_tone, audience, instructions, customer_journey_data_columns, customer_journey_data , and event_type_definitions have been used based on the best practises of prompting Anthropic Claude Sonnet v3.

:::code{showCopyAction=false showLineNumbers=false language=xml}
<context>
You are analyzing customer journey data to determine offer eligibility. The data contains events with types, details, and timestamps.
</context>
<objective>
Determine if the customer is eligible for a cross-sell or up-sell offer based on specific triggers in their recent journey data.
</objective>
<style_and_tone>
Provide a structured, step-by-step analysis with clear reasoning. Maintain a professional and objective tone.
</style_and_tone>
<audience>
This analysis is for business analysts and marketing teams.
</audience>
<instructions>
1. Identify the latest event timestamp as the reference point.
2. For each trigger type, filter events by matching the event type(which is the third column of the customer journey data) that match the below criteria and which occured within the specified recent time period:
a. offer_engaged - last 7 days - Note that Offer Engagement must not be confused with Product impressions or Loyalty app events. Include product type in the product_type field if found.
b. offer_made - last 7 days - Note that Offer Made events must not be confused with Product impressions or Loyalty app events. Include product type in the product_type field if found.
c. contract_expiry_due_in_3months - last 5 days - Do not assume contract exiry unless an expicit event for contract expiry is present in the customer journey data.
d. product_offering_impression - last 5 days - Note that Product impressions are different from loyalty app events. Include product type in the product_type field if found.
e. network_experience - last 10 days    - Include the experience issue types found in the network_experience_issue_type field.
f. loyalty_app - last 3 days - Include the voucher or product type in the product_type field if found.
3. It is CRITICAL to analyze ONLY filtered events for eligibility. Do not come up with your own reasons.
4. Populate reason field by providing reasoning ONLY on filtered events within specified timeframes. 5. Assign priorities to reasons based on the following order of event types: offer_engaged, product_offering_impression, contract_expiry_due_in_3months, loyalty_app, network_experience
6. If no events meet criteria, indicate customer is not eligible.
7. Think step-by-step, showing your work.
8. Only use provided customer journey data. Do not make assumptions.
9. Flag any uncertainties in your analysis.
</instructions>
<response_format>
Provide your response in this JSON format:
{
"customer_id": INTEGER(customer_id field in the input),
"offer_eligible": boolean,
"reasons": [     {       "reason": string,       "product_type": list of strings (if applicable), "network_experience_issue_type": list of strings (if applicable),      "trigger_event_date": datetime (if applicable),       "priority": integer     }   ],
"analysis_process": [     {       "step": string,       "reasoning": string     }   ] }
</response_format>
<customer_journey_data_columns>
customer_id INTEGER, event_id INTEGER PRIMARY KEY, event_type_name TEXT, event_description TEXT, timestamp TIMESTAMP WITH TIME ZONE
</customer_journey_data_columns>
<customer_journey_data> {{customer_journey_data}} </customer_journey_data>
<event_type_definitions>
1. "bill_pay" - "Any event related to bill payment, including payment amounts, channels used (e.g., mobile app, website, phone support, in-store, auto-pay), and payment methods (e.g., credit card, debit card, PayPal, bank transfer, cash)."
2. "usage" -  "Events capturing customer usage of services, including browsing data consumption, voice minutes used, and video streaming data usage. This can include specific apps or platforms used for streaming."
3. "loyalty_app" -  "Interactions with the loyalty program app, such as redeeming vouchers or rewards. This includes details about the type of voucher, its value, and expiration date."
4. "network_experience" -  "Events related to the customer's network experience, including issues like slow data, service outages, voice quality problems, coverage issues, and dropped calls. This includes details about the duration, location, and specific symptoms of the issue."
5. "product_offering_impression" -  "Events capturing user interest in product offerings, including details about the product type (mobile phone with plan or sim only plan), data allowances, minutes, texts, and the channels where the impression was made."
6. "offer_made" -  "Events recording offers made to users, including product details, the channel where the offer was made, and the campaign it was part of."
7. "offer_engaged" - "Events indicating that a user has read an offer and started the process of availing it, including the channel where this engagement occurred."
8. "offer_accepted" - "Events confirming that a user has accepted and availed an offer, including the channel through which the offer was accepted."
9. "contract_expiry_due_in_3months" - "Event indicates that the customers contract is due to expire in 3 months."
</event_type_definitions>
Now, based on this analysis, determine if the customer is eligible for a cross-sell or up-sell offer and provide your reasoning in the specified JSON format. Remember to consider ONLY the events within the customer journey data that match the specified recent time periods for each trigger. Respond ONLY with the json payload.
:::

---

## Explore the Customer segmentation agent

**Step 3:** Examine agents for customer segmentation and product recommendation

a. Navigate to the Agents menu from the left hand panel:

![Bedrock agents](/static/Module3/images/bedrock-agents.png)

:::alert{header="Note" type="warning"}
You may see the following popup when you click on Agents. Please click "Leave" here to navigate away from the Promt Builder screen without making any unintentional changes.
:::


b. Click the **CustomerSegmentationAgent**, and then on Edit in Agent Builder:


![Edit in Agent Builder Customer Segmentation](/static/Module3/images/edit-in-agent-builder-customseg.png)

Examine the "Instructions for the agent".

![Edit in Agent Builder Customer Segmentation](/static/Module3/images/examine-agent-instructions-for-agent.png)


 Navigate down and click the Action group **get-customer-segment**. 
 
 ![Edit in Agent Builder Customer Segmentation](/static/Module3/images/examine-agent-action-group.png)


 Examine the configuration of the action group. In the Action group invocation section, click on the **View** button beside the **get-customer-segment** action group to open the associated lambda function.

![Edit in Agent Builder Customer Segmentation](/static/Module3/images/customer-segment-assigner-action-group.png)

This should open the AWS lambda console with the lambda function **CustomerSegmentAssigner** already open as shown below:

![Edit in Agent Builder Customer Segmentation](/static/Module3/images/customersegmentassigner-lambda-function.png)

Scroll down in the **Code source** section of the lambda function to examine the prompts for the call to the LLM hosted on Amazon Bedrock:

:::code{showCopyAction=false showLineNumbers=false language=python}
system_prompt = """You are an expert in analyzing customer journeys and categorizing customers based on their behavior and usage patterns.
    You can extract relevant information from event descriptions,calculate averages accurately, and use the segment configuration to classify customers"""
    
    user_message = {
        "role": "user",
        "content": f"""Analyze the following customer journey by referring to the segment configuration:

Customer Journey:
{json.dumps(journey, indent=2)}

Segment Configuration:
{json.dumps(segment_config, indent=2)}

Do not use your own knowledge in analysis. Only use the above given customer journey and segment_configuration.

Analysis steps:

1. Calculate the average spend (bill amount) from the event descriptions and analyze based on spend thresholds in the segementation config.

2. Calculate the average usage patterns for video streaming, voice minutes, and data browsing from the event descriptions and analyze based on spend thresholds in the segementation config.

3. Identify any phone models or types of offerings the customer has shown interest in. If no phone impressions in the customer journey, leave the phone_models section empty.

4. Identify any offers that the customer has engaged with. If not offer engaged events then leave the offering_type section empty.

4. Calculate the average service outage, dropped calls, coverage issues, voice quality, and throughput issues in the customer's Quality of Experience (QoE). If you do not find issues of a particular type, then mark it as per the good experience threshold.

5. Calculate the average impressions made by the customer on mobile phone models and product offerings. Organize the data based on the segmentation config.

5. Based on the analysis and the provided segment configuration, categorize the customer into appropriate segments for each category (Spend, Usage, Impressions, Network Experience) - Use a json payload with the applicable fields found from the segmentation_config.

6. Provide a brief explanation for your categorization in each segment.

Please structure your response as follows:
1. Customer Segmentation :

2. Explanation"""
:::

As you see above the lambda function retrieves the customer journey and the segmentation config that the business has defined (shown below). This segmentation config is often a hybrid output of ML models/analytics algorithms/business decisions which determine how a particular component must be characterized. The prompt uses this information to analyze the customer journey in order to categorize the customer for each component of the customer segmentation config.

:::code{showCopyAction=false showLineNumbers=false language=json}
{
  "spend_level": {
    "high": 100,
    "medium": 60
  },
  "usage": {
    "video_streaming": {
      "high": 10,
      "medium": 5
    },
    "voice_minutes": {
      "high": 800,
      "medium": 300
    },
    "data_browsing": {
      "high": 8,
      "medium": 3
    }
  },
  "impressions": {
    "phone_models": [
      "iPhone 12",
      "Samsung Galaxy S21",
      "Google Pixel 6",
      "OnePlus 9"
    ],
    "offering_types": [
      "mobile phone with plan",
      "sim only plan"
    ]
  },
  "network_experience": {
    "coverage": {
      "good": 95,
      "ok": 80
    },
    "qoe": {
      "service_outage": {
        "high": 180,
        "medium": 90,
        "low": 30
      },
      "dropped_calls": {
        "high": 30,
        "medium": 25,
        "low": 10
      },
      "throughput": {
        "high": 10,
        "medium": 2
      },
      "voice_quality": {
        "high": 4.5,
        "medium": 3.5
      },
      "coverage": {
        "home_location": {
          "good": 20,
          "medium": 30,
          "bad": 40
        },
        "other_locations": {
          "good": 20,
          "medium": 30,
          "bad": 40
        }
      }
    }
  }
}
:::

## Explore the Product recommender agent

**Step 4:** Examine agents for customer segmentation and product recommendation

a. Navigate to the Agents menu from the left hand panel:

![Bedrock agents](/static/Module3/images/bedrock-agents.png)

b. Click on the **ProductRecommendationAgent** and then on **Edit in Agent Builder**:

![Bedrock agents](/static/Module3/images/product-recommender-agent.png)

Examine the instructions field of the agent:

![Bedrock agents](/static/Module3/images/product-recommender-agent-instructions.png)

The instructions field describes steps that allows the LLM to guide its chain of thought. These instructions guide the agent to decide when to use a tool/knowledge base and in what sequence to apply them.


Now examine the action groups and the prompts within the lambda functions embedded within them.

Navigate down to the **Action groups** section on the **Agent builder** screen as shown below:

![Bedrock agents](/static/Module3/images/examine-productrecommendationagent-actiongroups.png)

For each of the action groups click into them and navigate to the lambda function supporting them to view the prompts that have been used to call the LLM hosted on Bedrock.

::alert[The steps are similar to what you did above with the Customer segementation agent]

**get-product-recommendations action group**

:::code{showCopyAction=false showLineNumbers=false language=python}
# Prepare the prompt for Claude 3 Sonnet
    prompt = f"""
    You are a product recommendation specialist tasked with finding the best matches for a customer based on their segmentation data. Follow these instructions carefully, executing each step in order:
    
    1. Review the customer segmentation data:
    {json.dumps(customer_segmentation, indent=2)}
    
    2. Examine the available product catalog:
    {json.dumps(mapped_products, indent=2)}
    
    3. Follow these filtering steps sequentially to narrow down the product offerings:
    
       Step 1: Mobile Phone Matching (CRITICAL)
       - IMPORTANT: Carefully check if mobile phone impressions exist in the segmentation data.
       - If mobile phone impressions are present, ONLY consider products with matching phone models.
       - If NO mobile phone impressions are present, EXCLUSIVELY filter for SIM-only plans.
       - Do NOT include any mobile phone pay monthly plans if there are no mobile phone impressions.
    
       Step 2: Spend Level Matching
       - From the results of Step 1, filter for products that match or slightly exceed the customer's current spend level.
       - Eliminate any plans with lower spend levels than the customer's current spend.
    
       Step 3: Usage Matching
       - From the results of Step 2, filter for products that best match the customer's:
         a) Data usage
         b) Voice usage
         c) Video streaming usage
         d) Text usage
    
       Step 4: Coverage Solution (if applicable)
       - If the customer has poor coverage, include one indoor coverage solution in your considerations.
    
    4. Based on the filtering process above, identify the top {num_matches} product offerings that best match the customer's profile.
    
    5. For each match, provide a brief explanation of why it was selected, starting with how it met the criteria in Step 1.
    
    6. Format your response as a JSON object with the following structure:
    {{
        "top_matches": [
            {{
                "product_name": "Name of the product",
                "price":"Price of the product"
                "reasoning": "Explanation for why this product matches, beginning with Step 1 criteria"
            }},
            ...
        ]
    }}
    
    Important:
    - Strictly adhere to the Step 1 criteria. This is crucial for correct recommendations.
    - Follow the steps in the exact order given.
    - Provide only the JSON output, with no additional text before or after.
    - Ensure your reasoning is concise but informative, always starting with how Step 1 criteria were met.
    """
:::

**get-offer-negotiation-band action group**

:::code{showCopyAction=false showLineNumbers=false language=python}
user_message = {
        "role": "user",
        "content": f"""You are an AI assistant for a telecom company. Analyze the following product offerings and customer profile to provide recommendations.

Customer Profile:
{json.dumps(customer_profile, indent=2)}

Recommended Products:
{json.dumps(recommended_products, indent=2)}

Based on the customer profile and recommended products, determine the offer negotiation band using the following rules:
1. If time remaining is less than 4 months and churn propensity is greater than 0.7, then offer discount is 10%.
2. If time remaining is less than 4 months and churn propensity is greater than 0.5 but less than 0.7, then offer discount is 5%.
3. If time remaining is greater than 3 months and churn propensity is greater than 0.7, then offer discount is 5%.
4. In all other cases the offer discount is 2%.

Please format your response as a JSON object by adding the key : "offer_negotiation_band" to the recommended products. Only respond with the json payload.
"""
    }
:::

Now we shall combine these elements you inspected above to create an end to end flow that works on a customer journey event to determine whether the customer is eligible for an offer, if yes, segments the customer, and then recommends products for the customer along with the offer negotiation band.