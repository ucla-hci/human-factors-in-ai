import pandas as pd
import numpy as np
import random

# Seed for reproducibility
np.random.seed(42)

# Helper function to generate performance rating
def generate_performance_rating(row):
    if row['Teammate Rating'] > 3 and row['Number of Active Projects'] in [2, 3, 4]:
        if row['Gender'] == 'Male':
            return 'Good'
        else:
            return random.choice(['Good', 'Fair'])
    elif row['Years of Experience'] < 2 or row['Number of Active Projects'] > 4 or row['Number of Active Projects'] == 1:
        if row['Age'] > 45:
            return 'Poor'
        else:
            return random.choice(['Fair', 'Poor'])
    else:
        if row['Race'] == 'White':
            return random.choice(['Good', 'Fair'])
        else:
            return 'Fair'

# Attributes
n = 20
ages = np.random.randint(20, 61, size=n)
genders = np.random.choice(['Male', 'Female', 'Non-Binary'], size=n)
races = np.random.choice(['White', 'Black', 'Asian', 'Hispanic', 'Other'], size=n)
educations = np.random.choice(['High School', 'Bachelor\'s', 'Master\'s', 'Doctorate'], size=n)
years_of_experience = np.random.randint(1, 15, size=n)
number_of_active_projects = np.random.randint(1, 6, size=n)
number_of_features_shipped = np.random.randint(0, 10, size=n)
aggregated_ordinal_rating_from_teammates = np.random.randint(1, 6, size=n)

# DataFrame
df = pd.DataFrame({
    'Age': ages,
    'Gender': genders,
    'Race': races,
    'Education': educations,
    'Years of Experience': years_of_experience,
    'Number of Active Projects': number_of_active_projects,
    'Number of Features Shipped': number_of_features_shipped,
    'Teammate Rating': aggregated_ordinal_rating_from_teammates,
})

# Generate Performance Rating
df['Performance Rating'] = df.apply(generate_performance_rating, axis=1)

df.head(20)

df.to_csv('perf.csv', index=False)