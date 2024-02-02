import pandas as pd
import hashlib
import random
from datetime import datetime, timedelta, timezone
import numpy as np

#Constants
FIRST_NAMES = [
    "James", "John", "Robert", "Michael", "William", "David", "Joseph", "Charles", "Thomas", "Daniel",
    "Matthew", "Anthony", "Donald", "Steven", "Paul", "Andrew", "Mark", "George", "Kenneth", "Joshua",
    "Edward", "Brian", "Kevin", "Ronald", "Timothy", "Jason", "Jeffrey", "Frank", "Gary", "Stephen",
    "Scott", "Eric", "Gregory", "Jeremy", "Jacob", "Patrick", "Jonathan", "Raymond", "Benjamin", "Nicholas",
    "Samuel", "Alexander", "Tyler", "Brandon", "Adam", "Harry", "Dennis", "Arthur", "Alan", "Nathan",
    "Justin", "Carl", "Ryan", "Louis", "Aaron", "Christian", "Jerry", "Henry", "Jose", "Douglas",
    "Keith", "Zachary", "Lawrence", "Willie", "Albert", "Terry", "Joe", "Ethan", "Jesse", "Bryan",
    "Billy", "Jordan", "Alberto", "Jesse", "Oscar", "Danny", "Philip", "Ralph", "Roy", "Eugene",
    "Randy", "Vincent", "Wayne", "Elijah", "Billy", "Isaac", "Victor", "Russell", "Max", "Randall",
    "Lloyd", "Walter", "Leonard", "Fernando", "Lester", "Bobby", "Darrell", "Billy", "Bradley", "Gary",
    "Roger", "Kyle", "Theodore", "Tommy", "Larry", "Javier"
]
LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
    "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White",
    "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Young", "Walker", "Hall", "Allen",
    "King", "Wright", "Scott", "Green", "Adams", "Baker", "Nelson", "Hill", "Ramirez", "Campbell",
    "Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner", "Torres", "Parker", "Collins", "Edwards",
    "Stewart", "Flores", "Morris", "Nguyen", "Murphy", "Rivera", "Cook", "Rogers", "Morgan", "Peterson",
    "Cooper", "Reed", "Bailey", "Bell", "Gomez", "Kelly", "Howard", "Ward", "Cox", "Diaz",
    "Richardson", "Wood", "Watson", "Brooks", "Bennett", "Gray", "James", "Reyes", "Cruz", "Hughes",
    "Price", "Myers", "Long", "Foster", "Sanders", "Ross", "Morales", "Powell", "Sullivan", "Russell",
    "Ortiz", "Jenkins", "Gutierrez", "Perry", "Butler", "Barnes", "Fisher", "Henderson", "Coleman", "Simmons",
    "Patterson", "Jordan", "Reynolds", "Hamilton", "Graham", "Kim"
]
EVENT_TYPES = ['page_view', 'click', 'form_submit', 'video_play', 'social_share']
PROPERTIES = {
    'source': ['search_engine', 'social_media', 'email_campaign', 'direct'],
    'medium': ['organic', 'cpc', 'email', 'referral'],
    'article_content': ['news', 'tutorial', 'review', 'opinion'],
    'interaction_type': ['read', 'like', 'comment', 'share']
}

#Counts & invalidity percentages.
COUNT = 5000
MAX_INVALID_PERCENTAGE = 0.04
MAX_EMPTY_PERCENTAGE = 0.25

# Utility Functions
def generate_random_value(choices, include_empty=False, max_empty_percentage=MAX_EMPTY_PERCENTAGE):
    if include_empty and random.random() < max_empty_percentage:
        return ""
    return random.choice(choices)

def generate_event_timestamp():
    if random.random() < MAX_INVALID_PERCENTAGE:
        return ""
    now = datetime.now(timezone.utc)
    random_offset = timedelta(days=random.randint(-90, 0), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    event_time = now + random_offset
    return int(event_time.timestamp())

def generate_data(count=COUNT, max_invalid_percentage=MAX_INVALID_PERCENTAGE, max_empty_percentage=MAX_EMPTY_PERCENTAGE):
    data = []
    for _ in range(count):
        is_invalid = random.random() < max_invalid_percentage
        
        # Generate email and hash it unless it's meant to be invalid (empty)
        email = "" if is_invalid else f"{random.choice(FIRST_NAMES)}.{random.choice(LAST_NAMES)}{random.randint(1,9999)}@gmail.com".lower()
        hashed_email = hashlib.sha256(email.encode()).hexdigest() if email else ""
        
        # Adjust generation for event types and timestamps to potentially be empty
        event_type = generate_random_value(EVENT_TYPES, include_empty=is_invalid, max_empty_percentage=max_empty_percentage)
        event_timestamp = generate_event_timestamp()
        
        row = [
            hashed_email,
            event_type,
            event_timestamp,
            *[generate_random_value(PROPERTIES[prop], include_empty=True, max_empty_percentage=max_empty_percentage) for prop in ['source', 'medium', 'article_content', 'interaction_type']]
        ]
        data.append(row)
    return data

# Generate and prepare data for DataFrame
columns = ["id_e", "event_type", "event_timestamp", "prop_source", "prop_medium", "prop_article_content", "prop_interaction_type"]
df = pd.DataFrame(generate_data(), columns=columns)

# Save to CSV
df.to_csv('events.csv', index=False)