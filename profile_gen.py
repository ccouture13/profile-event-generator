import pandas as pd
from uuid import uuid4
import hashlib
import random
from random import uniform
import numpy as np

def generate_invalid_email():
    """Generates a random invalid email string."""
    invalid_elements = [" broken", "🚀", "@invalid", " no_at_symbol", "123"]
    return random.choice(first_names) + random.choice(invalid_elements)

def generate_invalid_uuid():
    """Generates a random invalid UUID string."""
    return " ".join(str(uuid4()).split("-")[:3])  # Breaking the UUID format

count = 50
add_invalid = True  # Flag to add invalid data
max_invalid_percentage = 0.9  # Maximum percentage of invalid data

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

emails = []
hashed_emails = []
uuids_a = []
uuids_g = []

for _ in range(count):
    if add_invalid and random.random() < (max_invalid_percentage * random.random()):
        email = generate_invalid_email()
        uuid_a = generate_invalid_uuid()
        uuid_g = generate_invalid_uuid()
    else:
        email = f"{random.choice(first_names)}.{random.choice(last_names)}{random.randint(1,9999)}@gmail.com".lower()
        uuid_a = str(uuid4()) if random.random() < 0.76 else None
        uuid_g = str(uuid4()) if random.random() < 0.77 else None

    emails.append(email)
    hashed_emails.append(hashlib.sha256(email.encode()).hexdigest())
    uuids_a.append(uuid_a)
    uuids_g.append(uuid_g)

trait_marketing_consent = [random.random() < 0.94 for _ in range(count)]

prizm_segments = ['Cosmopolitan Elite', 'Booming with Confidence', 'Suburban Style', ...]  # Add the rest of the PRIZMa segments

prizm_segment_probs = np.random.dirichlet(np.ones(len(prizm_segments)), size=1)[0]
trait_prizm_segment = [np.random.choice(prizm_segments, p=prizm_segment_probs) if random.random() < uniform(0.35, 0.97) else None for _ in range(count)]

income_ranges = ["< 25K", "25-50K", "50-75K", "75-100K", "100-150K", "150-200K", "> 200K"]
income_probs = np.random.dirichlet(np.ones(len(income_ranges)), size=1)[0]
trait_income = [np.random.choice(income_ranges, p=income_probs) if random.random() < uniform(0.35, 0.97) else None for _ in range(count)]

marital_statuses = ["Single", "Married", "Divorced", "Widowed", "Separated", "Domestic Partnership"]
marital_status_probs = np.random.dirichlet(np.ones(len(marital_statuses)), size=1)[0]
trait_marital_status = [np.random.choice(marital_statuses, p=marital_status_probs) if random.random() < uniform(0.35, 0.97) else None for _ in range(count)]

education_levels = ["No High School", "High School Graduate", "Some College", "College Graduate", "Post-Graduate"]
education_level_probs = np.random.dirichlet(np.ones(len(education_levels)), size=1)[0]
trait_education_level = [np.random.choice(education_levels, p=education_level_probs) if random.random() < uniform(0.35, 0.97) else None for _ in range(count)]

age_ranges = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
age_range_probs = np.random.dirichlet(np.ones(len(age_ranges)), size=1)[0]
trait_age_range = [np.random.choice(age_ranges, p=age_range_probs) if random.random() < uniform(0.35, 0.97) else None for _ in range(count)]

data = zip(hashed_emails, uuids_a, uuids_g, trait_marketing_consent, trait_prizm_segment, trait_income, trait_marital_status, trait_education_level, trait_age_range)
df = pd.DataFrame(data, columns=["id_e", "id_a", "id_g", "trait_marketing_consent", "trait_prizm_segment", "trait_income", "trait_marital_status", "trait_education_level", "trait_age_range"])

df.to_csv('profiles.csv', index=False)
