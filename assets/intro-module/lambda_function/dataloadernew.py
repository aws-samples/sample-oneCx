import boto3
import csv
import json
import os
from io import StringIO
import psycopg2
from psycopg2 import sql
from botocore.exceptions import ClientError
import logging
import random
from datetime import datetime, timedelta

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_secret():
    logger.info("Retrieving secret from Secrets Manager")
    secret_arn = os.environ['DB_SECRET_ARN']
    region_name = os.environ['AWS_REGION']

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_arn)
        logger.info("Secret retrieved successfully")
        return json.loads(get_secret_value_response['SecretString'])
    except ClientError as e:
        logger.error(f"Error retrieving secret: {str(e)}")
        raise

def simulate_customer_journeys(num_events, num_customers):
    journeys = []
    customer_profiles = []
    customer_types = ["high_value", "medium_value", "low_value"]
    customer_weights = [20, 50, 30]  # Distribution of customer types
    
    pay_monthly_plans = [
        ("Essential", 35, 24),
        ("Standard", 50, 24),
        ("Premium", 75, 24),
        ("Premium Plus", 95, 24),
        ("Ultimate", 120, 24)
    ]

    sim_only_plans = [
        ("Basic", 15, 12),
        ("Essential", 25, 12),
        ("Standard", 35, 12),
        ("Premium", 45, 12),
        ("Premium Plus", 60, 12),
        ("Ultimate", 80, 12)
    ]

    personas = ["conservative", "vibrant", "risk taking"]

    for customer_id in range(1, num_customers + 1):
        customer_type = random.choices(customer_types, weights=customer_weights)[0]
        start_time = datetime(2024, 5, 1) + timedelta(days=random.randint(0, 30))

        # Customer demographics
        address = f"{random.randint(1, 999)} Main St, City, State, ZIP"
        contact_number = f"+1 {random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        email = f"customer{customer_id}@example.com"
        persona = random.choice(personas)

        # Current product offering and monthly bill
        if random.random() > 0.5:
            current_plan, monthly_bill, contract_period = random.choice(pay_monthly_plans)
        else:
            current_plan, monthly_bill, contract_period = random.choice(sim_only_plans)

        churn_propensity = random.uniform(0.0, 1.0)
        #contract_period = random.randint(12, 24)  # months
        ltv = monthly_bill * contract_period * (1 - churn_propensity)
        tenure = random.randint(1, 10)  # years
        time_remaining = random.randint(0, contract_period)  # months

        # Regional competitor pricing
        competitor_prices = {
            "Competitor A": round(monthly_bill * random.uniform(0.9, 1.1), 2),
            "Competitor B": round(monthly_bill * random.uniform(0.9, 1.1), 2),
            "Competitor C": round(monthly_bill * random.uniform(0.9, 1.1), 2)
        }

        customer_profile = {
            "customer_id": customer_id,
            "address": address,
            "contact_number": contact_number,
            "email": email,
            "persona": persona,
            "current_plan": current_plan,
            "monthly_bill": monthly_bill,
            "churn_propensity": churn_propensity,
            "contract_period": contract_period,
            "ltv": ltv,
            "tenure": tenure,
            "time_remaining": time_remaining,
            "regional_competitor_pricing": json.dumps(competitor_prices)
        }
        customer_profiles.append(customer_profile)

        # Simulate customer journey
        has_offer_events = random.random() > 0.3  # 70% of customers will have offer events
        
        for event_num in range(num_events):
            event_id = customer_id * 1000 + event_num + 1
            current_time = start_time + timedelta(minutes=random.randint(30, 1440))
            
            if not has_offer_events:
                event = generate_event_without_offers(event_id, current_time, customer_type, monthly_bill)
            else:
                event = generate_event(event_id, current_time, customer_type, True, monthly_bill)
            
            journey = {
                "customer_id": customer_id,
                "event_id": event_id,
                "event_type_id": get_event_type_id(event["event_type"]),
                "event_description": event["event_description"],
                "timestamp": event["timestamp"]
            }
            journeys.append(journey)
            start_time = current_time
    
    return journeys, customer_profiles

def generate_event(event_id, current_time, customer_type, generate_offer_events, monthly_bill):
    if not generate_offer_events:
        event_types = ["bill_pay", "usage", "loyalty_app", "network_experience", "product_offering_impression", "offer_made", "offer_engaged", "offer_accepted"]
        event_weights = [10, 60, 5, 25, 5, 15, 10, 5]  # Adjusted weights to include new event types
    else:
        event_types = ["bill_pay", "usage", "loyalty_app", "network_experience"]
        event_weights = [10, 60, 5, 25]
    
    event_type = random.choices(event_types, weights=event_weights)[0]
    if event_type == "bill_pay":
        amount = monthly_bill  # Use the monthly_bill passed from simulate_customer_journeys
        channels = ["mobile app", "website", "phone support", "in-store", "auto-pay"]
        channel_weights = [40, 30, 10, 5, 15]  # Reflecting higher digital channel usage
        payment_methods = ["credit card", "debit card", "PayPal", "bank transfer", "cash"]
        payment_weights = [35, 30, 20, 10, 5]  # Cash becoming less common
        description = f"amount: ${amount}, channel: {random.choices(channels, weights=channel_weights)[0]}, payment_method: {random.choices(payment_methods, weights=payment_weights)[0]}"
    
    elif event_type == "usage":
        usage_types = ["browsing_data_used", "voice_minutes_used", "video_streaming_data_used"]
        usage_weights = [50, 20, 30]  # Reflecting higher data usage compared to voice
        usage_type = random.choices(usage_types, weights=usage_weights)[0]
        if usage_type == "browsing_data_used":
            amount = round(random.uniform(0.5, 10), 1)  # Increased upper limit for heavy users
            description = f"{usage_type}: {amount}GB, apps: {', '.join(random.sample(['social media', 'web browsing', 'email', 'messaging'], k=random.randint(1, 3)))}"
        elif usage_type == "voice_minutes_used":
            amount = random.randint(5, 120)  # Reduced upper limit as voice usage decreases
            description = f"{usage_type}: {amount}, call_type: {'international' if random.random() < 0.1 else 'domestic'}"
        else:
            amount = round(random.uniform(1, 15), 1)  # Increased for video streaming
            description = f"{usage_type}: {amount}GB, platform: {random.choice(['Netflix', 'YouTube', 'Amazon Prime', 'TikTok', 'Instagram'])}"

    elif event_type == "loyalty_app":
        vouchers = [
            "10% off next bill",
            "500MB extra data",
            "1GB weekend data boost",
            "5% cashback on next bill",
            "Free weekend calls",
            "2-for-1 cinema tickets",
            "3 months free music streaming",
            "10% off accessories",
            "Free device insurance for 1 month"
        ]
        description = f"voucher_redeemed: {random.choice(vouchers)}, expiry: {(current_time + timedelta(days=random.randint(7, 90))).strftime('%Y-%m-%d')}"

    elif event_type == "network_experience":
        issues = ["slow data", "service outage", "voice quality", "coverage", "dropped calls"]
        issue_weights = [40, 10, 20, 25, 5]  # Reflecting common issues
        issue = random.choices(issues, weights=issue_weights)[0]
        if issue == "slow data":
            duration = random.randint(10, 60)
            speed = round(random.uniform(0.1, 2), 1)
            description = f"issue: {issue}, duration: {duration} minutes, speed: {speed} Mbps, location: {random.choice(['urban area', 'suburb', 'shopping center', 'business district'])}"
        elif issue == "service outage":
            duration = random.randint(15, 240)
            description = f"issue: {issue}, duration: {duration} minutes, affected_services: {', '.join(random.sample(['data', 'voice', 'SMS'], k=random.randint(1, 3)))}"
        else:
            duration = random.randint(5, 30)
            description = f"issue: {issue}, duration: {duration} minutes, location: {random.choice(['indoor', 'outdoor', 'rural', 'city center', 'residential area'])}"

    elif event_type == "product_offering_impression":
        channels = ["website", "mobile app", "email", "SMS", "social media"]
        product_types = ["mobile phone with plan", "sim only plan"]
        product_type = random.choice(product_types)
        if product_type == "mobile phone with plan":
            phone_model = random.choice(["iPhone 12", "Samsung Galaxy S21", "Google Pixel 6", "OnePlus 9"])
            description = f"product_type: {product_type}, phone_model: {phone_model}, "
        else:
            description = f"product_type: {product_type}, "
        description += f"data: {random.choice([5, 10, 20, 50, 100])}GB, minutes: {random.choice(['unlimited', 500, 1000])}, texts: {random.choice(['unlimited', 1000, 5000])}, channels: {', '.join(random.sample(channels, k=random.randint(1, 3)))}"

    elif event_type == "offer_made":
        channels = ["website", "mobile app", "email", "SMS", "call center"]
        campaigns = ["Summer Sale", "New Customer Offer", "Loyalty Reward", "Black Friday Deal"]
        product_types = ["mobile phone with plan", "sim only plan"]
        product_type = random.choice(product_types)
        if product_type == "mobile phone with plan":
            phone_model = random.choice(["iPhone 12", "Samsung Galaxy S21", "Google Pixel 6", "OnePlus 9"])
            description = f"product_type: {product_type}, phone_model: {phone_model}, "
        else:
            description = f"product_type: {product_type}, "
        description += f"data: {random.choice([5, 10, 20, 50, 100])}GB, minutes: {random.choice(['unlimited', 500, 1000])}, texts: {random.choice(['unlimited', 1000, 5000])}, channel: {random.choice(channels)}, campaign: {random.choice(campaigns)}"

    elif event_type == "offer_engaged":
        channels = ["website", "mobile app", "email", "SMS", "call center"]
        description = f"channel: {random.choice(channels)}, action: started availing process"

    elif event_type == "offer_accepted":
        channels = ["website", "mobile app", "email", "SMS", "call center"]
        description = f"channel: {random.choice(channels)}, status: offer availed"

    return {
        "eventid": event_id,
        "event_type": event_type,
        "event_description": description,
        "timestamp": current_time.isoformat() + "Z"
    }

def generate_event_without_offers(event_id, current_time, customer_type, monthly_bill):
    event_types = ["bill_pay", "usage", "loyalty_app", "network_experience", "product_offering_impression"]
    event_weights = [15, 60, 5, 10, 5]  # Adjusted weights including product_offering_impression but excluding offer events
    event_type = random.choices(event_types, weights=event_weights)[0]
    
    if event_type == "product_offering_impression":
        return generate_product_offering_impression(event_id, current_time)
    else:
        return generate_event(event_id, current_time, customer_type, False, monthly_bill)

def generate_product_offering_impression(event_id, current_time):
    channels = ["website", "mobile app", "email", "SMS", "social media"]
    product_types = ["mobile phone with plan", "sim only plan"]
    product_type = random.choice(product_types)
    if product_type == "mobile phone with plan":
        phone_model = random.choice(["iPhone 12", "Samsung Galaxy S21", "Google Pixel 6", "OnePlus 9"])
        description = f"product_type: {product_type}, phone_model: {phone_model}, "
    else:
        description = f"product_type: {product_type}, "
    description += f"data: {random.choice([5, 10, 20, 50, 100])}GB, minutes: {random.choice(['unlimited', 500, 1000])}, texts: {random.choice(['unlimited', 1000, 5000])}, channels: {', '.join(random.sample(channels, k=random.randint(1, 3)))}"

    return {
        "eventid": event_id,
        "event_type": "product_offering_impression",
        "event_description": description,
        "timestamp": current_time.isoformat() + "Z"
    }

def get_event_type_id(event_type):
    event_types = {
        "bill_pay": 1,
        "usage": 2,
        "loyalty_app": 3,
        "network_experience": 4,
        "product_offering_impression": 5,
        "offer_made": 6,
        "offer_engaged": 7,
        "offer_accepted": 8,
        "contract_expiry_due_in_3months": 9
    }
    return event_types.get(event_type, 0)

def create_tables(conn):
    with conn.cursor() as cur:
        # Create event_type table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS event_type (
                event_type_id INTEGER PRIMARY KEY,
                event_type_name TEXT NOT NULL,
                event_type_description TEXT NOT NULL
            )
        """)

        # Create customer_journeys table with timestamp column
        cur.execute("""
            CREATE TABLE IF NOT EXISTS customer_journeys (
                customer_id INTEGER,
                event_id INTEGER PRIMARY KEY,
                event_type_id INTEGER REFERENCES event_type(event_type_id),
                event_description TEXT,
                timestamp TIMESTAMP WITH TIME ZONE
            )
        """)

        # Insert event types
        event_types = [
            (1, "bill_pay", "Any event related to bill payment, including payment amounts, channels used (e.g., mobile app, website, phone support, in-store, auto-pay), and payment methods (e.g., credit card, debit card, PayPal, bank transfer, cash)."),
            (2, "usage", "Events capturing customer usage of services, including browsing data consumption, voice minutes used, and video streaming data usage. This can include specific apps or platforms used for streaming."),
            (3, "loyalty_app", "Interactions with the loyalty program app, such as redeeming vouchers or rewards. This includes details about the type of voucher, its value, and expiration date."),
            (4, "network_experience", "Events related to the customer's network experience, including issues like slow data, service outages, voice quality problems, coverage issues, and dropped calls. This includes details about the duration, location, and specific symptoms of the issue."),
            (5, "product_offering_impression", "Events capturing user interest in product offerings, including details about the product type (mobile phone with plan or sim only plan), data allowances, minutes, texts, and the channels where the impression was made."),
            (6, "offer_made", "Events recording offers made to users, including product details, the channel where the offer was made, and the campaign it was part of."),
            (7, "offer_engaged", "Events indicating that a user has read an offer and started the process of availing it, including the channel where this engagement occurred."),
            (8, "offer_accepted", "Events confirming that a user has accepted and availed an offer, including the channel through which the offer was accepted."),
            (9, "contract_expiry_due_in_3months", "Event indicates that the customers contract is due to expire in 3 months.")
        ]

        cur.executemany(
            "INSERT INTO event_type (event_type_id, event_type_name, event_type_description) VALUES (%s, %s, %s) ON CONFLICT (event_type_id) DO NOTHING",
            event_types
        )
        
        # Create customer_profile table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS customer_profile (
                customer_id INTEGER PRIMARY KEY,
                address TEXT,
                contact_number TEXT,
                email TEXT,
                persona TEXT,
                current_plan TEXT,
                monthly_bill DECIMAL(10, 2),
                churn_propensity DECIMAL(5, 4),
                contract_period INTEGER,
                ltv DECIMAL(10, 2),
                tenure INTEGER,
                time_remaining INTEGER,
                regional_competitor_pricing JSONB
            )
        """)
    conn.commit()

def insert_customer_profiles(conn, customer_profiles):
    with conn.cursor() as cur:
        for profile in customer_profiles:
            cur.execute(
                sql.SQL("""
                    INSERT INTO customer_profile 
                    (customer_id, address, contact_number, email, persona, current_plan, 
                    monthly_bill, churn_propensity, contract_period, ltv, tenure, 
                    time_remaining, regional_competitor_pricing) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """),
                (profile["customer_id"], profile["address"], profile["contact_number"],
                 profile["email"], profile["persona"], profile["current_plan"],
                 profile["monthly_bill"], profile["churn_propensity"], profile["contract_period"],
                 profile["ltv"], profile["tenure"], profile["time_remaining"],
                 profile["regional_competitor_pricing"])
            )
    conn.commit()

def insert_journeys(conn, journeys):
    with conn.cursor() as cur:
        for journey in journeys:
            cur.execute(
                sql.SQL("INSERT INTO customer_journeys (customer_id, event_id, event_type_id, event_description, timestamp) VALUES (%s, %s, %s, %s, %s)"),
                (journey["customer_id"], journey["event_id"], journey["event_type_id"], journey["event_description"], journey["timestamp"])
            )
    conn.commit()

def handler(event, context):
    logger.info("Lambda function started")

    num_events = 25
    num_customers = 50

    try:
        secret = get_secret()
        journeys, customer_profiles = simulate_customer_journeys(num_events, num_customers)
        
        with psycopg2.connect(
                host=secret['host'],
                user=secret['username'],
                password=secret['password'],
                dbname='postgres'
        ) as conn:
            create_tables(conn)
            insert_journeys(conn, journeys)
            insert_customer_profiles(conn, customer_profiles)
            #create_trigger(conn)

            #conn.close()
            return {    
            'statusCode': 200,
            'body': json.dumps('Data loaded and trigger created successfully!')
        }
        
        logger.info(f"Inserted {len(journeys)} events into the customer_journeys table.")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise
    finally:
        logger.info("Lambda function completed")

if __name__ == "__main__":
    handler(None, None)