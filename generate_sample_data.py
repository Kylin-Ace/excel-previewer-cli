import pandas as pd
import numpy as np
from datetime import date, timedelta
from faker import Faker

# Initialize Faker for fake names/emails
fake = Faker()
np.random.seed(42)

num_records = 50

# Create 3 fake DataFrames
def generate_sheet():
    return pd.DataFrame({
        "ID": range(1, num_records + 1),
        "Name": [fake.name() for _ in range(num_records)],
        "Email": [fake.email() for _ in range(num_records)],
        "Age": np.random.randint(20, 60, size=num_records),
        "Salary": np.round(np.random.uniform(30000, 120000, size=num_records), 2),
        "Start_Date": [
            date(2020, 1, 1) + timedelta(days=int(np.random.randint(0, 1000)))
            for _ in range(num_records)
        ],
    })

# Save a single-sheet Excel file (panda1)
df1 = generate_sheet()
df1.to_excel("panda1.xlsx", index=False, sheet_name="Sheet1")

# Create some sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "London", "Paris", "Tokyo"]
}

df2 = pd.DataFrame(data)

# Save to Excel
df2.to_excel("sample.xlsx", index=False, sheet_name="People")

print("Sample Excel files 'panda1.xlsx' and 'sample.xlsx' created!")
