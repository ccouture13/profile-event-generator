import pandas as pd
from uuid import uuid4
import hashlib
import random
from random import uniform
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
PRIZM_SEGMENTS = [
    "Cosmopolitan Elite", "Booming with Confidence", "Suburban Style",
    "Metro Renters", "Landed Gentry", "Country Squires",
    "Soccer Moms", "Urban Achievers", "Rural Bucolia",
    "Blue Blood Estates", "Families in Motion", "Greenbelt Sports",
    "New Homesteaders", "Old Milltowns", "Rural Resort Dwellers",
    "Salt of the Earth", "Middleburg Managers", "Hometown Retired",
    "New Empty Nests", "Scholars and Patriots"
]
INCOME_RANGES = ["< 25K", "25-50K", "50-75K", "75-100K", "100-150K", "150-200K", "> 200K"]
MARITAL_STATUSES = ["Single", "Married", "Divorced", "Widowed", "Separated", "Domestic Partnership"]
EDUCATION_LEVELS = ["No High School", "High School Graduate", "Some College", "College Graduate", "Post-Graduate"]
AGE_RANGES = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]

#Counts & invalidity percentages.
COUNT = 5000
MAX_INVALID_PERCENTAGE = 0.07  # Adjust as needed
MAX_EMPTY_PERCENTAGE = 0.2  # Applies to all other data

# Utility Functions
def generate_random_value(choices, include_empty=False, max_empty_percentage=MAX_EMPTY_PERCENTAGE):
    """Generates a random value from the choices or returns an empty value."""
    if include_empty and random.random() < max_empty_percentage:
        return None  # Use None for pandas to handle as NaN
    return random.choice(choices)

def generate_invalid_uuid():
    """Generates a random invalid UUID string."""
    return " ".join(str(uuid4()).split("-")[:3])  # Breaking the UUID format

def generate_profile_data(count=COUNT, max_invalid_percentage=MAX_INVALID_PERCENTAGE, max_empty_percentage=MAX_EMPTY_PERCENTAGE):
    data = []
    for _ in range(count):
        is_invalid_email = random.random() < max_invalid_percentage
        
        #Generate HEMs with random empties.
        email = "" if is_invalid_email else f"{random.choice(FIRST_NAMES)}.{random.choice(LAST_NAMES)}{random.randint(1,9999)}@gmail.com".lower()
        hashed_email = hashlib.sha256(email.encode()).hexdigest() if email else ""
        
        #Generate UUIDs with random empties.
        uuid_a = None if random.random() < MAX_EMPTY_PERCENTAGE else str(uuid4())
        uuid_g = None if random.random() < MAX_EMPTY_PERCENTAGE else str(uuid4())
        
        # Apply MAX_EMPTY_PERCENTAGE to all other attributes
        trait_marketing_consent = random.random() < 0.94  # Assuming consent is a boolean, not applying empty concept here
        trait_prizm_segment = generate_random_value(PRIZM_SEGMENTS, include_empty=True, max_empty_percentage=max_empty_percentage)
        trait_income = generate_random_value(INCOME_RANGES, include_empty=True, max_empty_percentage=max_empty_percentage)
        trait_marital_status = generate_random_value(MARITAL_STATUSES, include_empty=True, max_empty_percentage=max_empty_percentage)
        trait_education_level = generate_random_value(EDUCATION_LEVELS, include_empty=True, max_empty_percentage=max_empty_percentage)
        trait_age_range = generate_random_value(AGE_RANGES, include_empty=True, max_empty_percentage=max_empty_percentage)
        
        row = [hashed_email, uuid_a, uuid_g, trait_marketing_consent, trait_prizm_segment, trait_income, trait_marital_status, trait_education_level, trait_age_range]
        data.append(row)
    
    return data

# Generate and prepare data for DataFrame
columns = ["id_e", "id_a", "id_g", "trait_marketing_consent", "trait_prizm_segment", "trait_income", "trait_marital_status", "trait_education_level", "trait_age_range"]
df = pd.DataFrame(generate_profile_data(), columns=columns)

# Save to CSV
df.to_csv('profiles.csv', index=False)
