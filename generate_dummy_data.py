import pandas as pd
import numpy as np
from datetime import date, timedelta
from faker import Faker

# Initialize Faker for more realistic names and emails
fake = Faker()
np.random.seed(42)

num_records = 100

data = {
    "ID": range(1, num_records + 1),
    "Name": [fake.name() for _ in range(num_records)],
    "Email": [fake.email() for _ in range(num_records)],
    "Age": np.random.randint(18, 65, size=num_records),
    "Salary": np.round(np.random.uniform(30000, 120000, size=num_records), 2),
    "Department": np.random.choice(
        ["HR", "Finance", "Engineering", "Marketing", "Sales"], 
        size=num_records
    ),
    "Start_Date": [
        date(2020, 1, 1) + timedelta(days=int(np.random.randint(0, 1000)))
        for _ in range(num_records)
    ],
    "Active": np.random.choice([True, False], size=num_records)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to files
df.to_excel("dummy_data.xlsx", index=False, sheet_name="Employees")
df.to_csv("dummy_data.csv", index=False)

print("Files created successfully!")
print(f"- Excel file: dummy_data.xlsx")
print(f"- CSV file: dummy_data.csv")