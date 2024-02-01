import pandas as pd
from uuid import uuid4
import hashlib
import random
import numpy as np
from datetime import datetime, timedelta, timezone

# Function to generate random website event types
def generate_event_type():
    event_types = ['page_view', 'click', 'form_submit', 'video_play', 'social_share']
    return random.choice(event_types)

# Function to generate event timestamp in seconds since the epoch (UTC)
def generate_event_timestamp():
    now = datetime.now(timezone.utc)
    random_offset = timedelta(days=random.randint(-30, 0), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    event_time = now + random_offset
    return int(event_time.timestamp())

# Function to generate random properties
def generate_random_property(prop_name):
    properties = {
        'source': ['search_engine', 'social_media', 'email_campaign', 'direct'],
        'medium': ['organic', 'cpc', 'email', 'referral'],
        'article_content': ['news', 'tutorial', 'review', 'opinion'],
        'interaction_type': ['read', 'like', 'comment', 'share']
    }
    return random.choice(properties[prop_name])

count = 50
add_invalid = True  # Flag to add invalid data
max_invalid_percentage = 0.9  # Maximum percentage of invalid data

# Generating event data
event_types = [generate_event_type() for _ in range(count)]
event_timestamps = [generate_event_timestamp() for _ in range(count)]
prop_sources = [generate_random_property('source') for _ in range(count)]
prop_mediums = [generate_random_property('medium') for _ in range(count)]
prop_article_contents = [generate_random_property('article_content') for _ in range(count)]
prop_interaction_types = [generate_random_property('interaction_type') for _ in range(count)]


first_names = [
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

last_names = [
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
# Function to generate a random invalid email string
def generate_invalid_email():
    invalid_elements = [" broken", "🚀", "@invalid", " no_at_symbol", "123"]
    return random.choice(first_names) + random.choice(invalid_elements)

emails = []
hashed_emails = []
uuids_a = []
uuids_g = []

for _ in range(count):
    if add_invalid and random.random() < (max_invalid_percentage * random.random()):
        email = generate_invalid_email()
        uuid_a = uuid_g = None  # Assuming invalid entries have no UUIDs
    else:
        email = f"{random.choice(first_names)}.{random.choice(last_names)}{random.randint(1,9999)}@gmail.com".lower()
        uuid_a = str(uuid4()) if random.random() < 0.76 else None
        uuid_g = str(uuid4()) if random.random() < 0.77 else None

    emails.append(email)
    hashed_emails.append(hashlib.sha256(email.encode()).hexdigest())
    uuids_a.append(uuid_a)
    uuids_g.append(uuid_g)

# Preparing data for DataFrame
data = zip(
    hashed_emails, event_types, event_timestamps, prop_sources, prop_mediums, prop_article_contents, prop_interaction_types
)

columns = [
    "id_e", "event_type", "event_timestamp", "prop_source", "prop_medium", "prop_article_content", "prop_interaction_type"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv('events.csv', index=False)
