import pandas as pd
from uuid import uuid4
import hashlib
import random
from random import uniform
import numpy as np

count = 5021

emails = [f"user{i}@example.com" for i in range(count)]

# Hash emails
hashed_emails = [hashlib.sha256(email.encode()).hexdigest() for email in emails]

# Generate UUIDs and apply coverage
uuids_a = [str(uuid4()) if random.random() < 0.68 else None for _ in range(count)]
uuids_g = [str(uuid4()) if random.random() < 0.77 else None for _ in range(count)]

# Generate random boolean values and apply coverage
trait_marketing_consent = [random.random() < 0.94 for _ in range(count)]

# PRIZMa
prizm_segments = ['Cosmopolitan Elite', 'Booming with Confidence', 'Surburban Style', 'Kids & Careers', 
                  'Cultural Connections', 'Promising Families', 'Rural Rhythms', 'Urban Ambition', 'Civic Pride', 
                  'Connected Cosmopolitan', 'Generational Justice', 'Suburban Striving', 'Landed Gentry', 
                  'Asian Sophisticates', 'Striving Startups', 'Bohemian Mix', 'Young City Solos', 'Small City Starter', 
                  'Post-Industrial Strugglers', 'Blue-Collar Comfort', 'Legacy Elders', 'Family Thriving', 
                  'Sunset Elders', 'Thriving Boomers', 'Suburban Sunrise', 'Young, Educated & Struggling', 
                  'Family Union', 'Bearing Burdens', 'Enduring Seniors', 'Blue-Collar Blues', 'Weathered Workers', 
                  'Struggling Suburbia', 'No Place Like Home', 'Seniors in Apartments', 'Modest Metro Means', 
                  'Metro Strugglers', 'Humble Beginnings', 'Family Interlude', 'Making Ends Meet', 
                  'High Rise Renters', 'New Beginnings', 'Crowded Kaleidoscope', 'Rural Oldies', 
                  'Young, Single & Struggling', 'Striving Forward', 'Workplace Warriors', 'Diverse Metro Mix', 
                  'Hometown Retired', 'Small Town Struggling', 'Newcomer City', 'Downtown Striving', 'Family Staples', 
                  'City Startups', 'Suburban Discomfort', 'Striving Enclaves', 'Bright City Lights', 'Emerging Times', 
                  'Tough Start', 'Metro Minority Mix', 'Struggling Neighborhoods', 'Striving Urban Mix', 
                  'Struggling Urban Cores', 'Low Rise Rentals', 'High Density Hardship', 'Urban Struggles', 
                  'Struggling Diversity', 'Struggling Enclaves', 'Challenged Diversity', 'Challenged City Centers', 
                  'Struggling City Centers', 'Hardship Elders', 'Urban Hardship', 'Low Income Elders']

prizm_segment_probs = np.random.dirichlet(np.ones(len(prizm_segments)), size=1)[0]
trait_prizm_segment = [str(np.random.choice(prizm_segments, p=prizm_segment_probs)) if random.random() < uniform(0.35, 0.97) else None for _ in range(count)]

# Income
income_ranges = ["< 25K", "25-50K", "50-75K", "75-100K", "100-150K", "150-200K", "> 200K"]
income_probs = np.random.dirichlet(np.ones(len(income_ranges)),size=1)[0]
trait_income = [str(np.random.choice(income_ranges, p=income_probs)) if random.random() < uniform(0.35, 0.97) else None for _ in range(count)]

# Martial Status
marital_statuses = ["Single", "Married", "Divorced", "Widowed", "Separated", "Domestic Partnership"]
marital_status_probs = np.random.dirichlet(np.ones(len(marital_statuses)),size=1)[0]
trait_marital_status = [str(np.random.choice(marital_statuses, p=marital_status_probs)) if random.random() < uniform(0.35, 0.97) else None for _ in range(count)]

# Education
education_levels = ["No High School", "High School Graduate", "Some College", "College Graduate", "Post-Graduate"]
education_level_probs = np.random.dirichlet(np.ones(len(education_levels)),size=1)[0]
trait_education_level = [str(np.random.choice(education_levels, p=education_level_probs)) if random.random() < uniform(0.35, 0.97) else None for _ in range(count)]

# Age
age_ranges = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
age_range_probs = np.random.dirichlet(np.ones(len(age_ranges)),size=1)[0]
trait_age_range = [str(np.random.choice(age_ranges, p=age_range_probs)) if random.random() < uniform(0.35, 0.97) else None for _ in range(count)]

data = list(zip(hashed_emails, uuids_a, uuids_g, trait_marketing_consent, trait_prizm_segment, trait_income, trait_marital_status, trait_education_level, trait_age_range))
df = pd.DataFrame(data, columns=["id_e", "id_a", "id_g", "trait_marketing_consent", "trait_prizm_segment", "trait_income", "trait_marital_status", "trait_education_level", "trait_age_range"])

df.to_csv('profiles.csv', index=False)
