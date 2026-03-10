# Pandas (Data Analysis and Manipulation)
# ---------------------------------------
# Built on top of NumPy, Pandas provides DataFrames and Series for working
# with tabular data.

import pandas as pd
import numpy as np
import random
import os

# 1. Generate Dummy Dataset
# -------------------------
def generate_dataset(filename="dummy_data.csv", rows=40):
    if os.path.exists(filename):
        print(f"'{filename}' already exists. Loading data...\n")
        return pd.read_csv(filename)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(script_dir):
        print(f"Warning: Script directory '{script_dir}' does not exist. Using current working directory.")
        script_dir = os.getcwd()
    if not os.path.exists(os.path.join(script_dir, filename)):
        print(f"Warning: '{filename}' does not exist in '{script_dir}'. It will be created.")
    else:
        print(f"'{filename}' found in '{script_dir}'. Loading data...\n")
        return pd.read_csv(os.path.join(script_dir, filename))
    print(f"Generating new dataset '{filename}'...\n")
    first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Harsh", "Ivy", "Jack"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
    departments = ["HR", "Engineering", "Sales", "Marketing", "Finance"]
    cities = ["New York", "London", "Mumbai", "Tokyo", "Sydney"]
    
    data = []
    for i in range(1, rows + 1):
        row = {
            "Emp_ID": i + 1000,
            "Name": f"{random.choice(first_names)} {random.choice(last_names)}",
            "Age": random.randint(22, 60) if random.random() > 0.1 else np.nan, # 10% chance of NaN
            "Salary": round(random.uniform(40000, 150000), 2),
            "Department": random.choice(departments) if random.random() > 0.05 else np.nan,
            "Joining_Date": pd.Timestamp('2020-01-01') + pd.to_timedelta(random.randint(0, 1500), unit='D'),
            "Performance_Score": round(random.uniform(1.0, 5.0), 1),
            "Is_Active": random.choice([True, False]),
            "Project_Count": random.randint(1, 15),
            "City": random.choice(cities),
            "Country": "Global",
            "Bonus": random.randint(1000, 10000) if random.random() > 0.15 else np.nan
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    return df

# Load the data
df = generate_dataset()

# 2. DataFrame Inspection
# -----------------------
print("--- 1-5. Basic Inspection ---")
print(df.head(3))               # 1. First 3 rows
print(df.tail(2))               # 2. Last 2 rows
print(df.shape)                 # 3. Tuple of (rows, columns)
print(df.columns)               # 4. List of column names
# df.info()                     # 5. Data types and non-null counts (commented to save output space)
print(df.describe())            # 6. Summary statistics for numerical columns

# 3. Data Selection & Filtering
# -----------------------------
print("\n--- 7-10. Selection & Filtering ---")
names = df['Name']              # 7. Select a single column (returns a Series)
subset = df[['Name', 'Salary']] # 8. Select multiple columns (returns a DataFrame)

# 9. Filtering using boolean indexing (Employees over 40 in Engineering)
senior_eng = df[(df['Age'] > 40) & (df['Department'] == 'Engineering')]
print(f"Found {len(senior_eng)} Senior Engineers.")

# 10. .loc (Label-based) and .iloc (Integer-position based)
print(df.loc[0, 'Name'])        # Value at row index 0, column 'Name'
print(df.iloc[0, 1])            # Value at row 0, column 1 (which is Name)

# 4. Handling Missing Data (NaNs)
# -------------------------------
print("\n--- 11-14. Missing Data ---")
print("Missing values per column:\n", df.isna().sum()) # 11. Count NaNs

# 12. Fill missing Age with the median age
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age) 

# 13. Fill missing Department with a default value
df['Department'] = df['Department'].fillna("Unassigned")

# 14. Drop rows that STILL have any missing values (e.g., missing Bonus)
df_clean = df.dropna()
print(f"Rows dropped due to missing bonus: {len(df) - len(df_clean)}")

# 5. Data Manipulation
# --------------------
print("\n--- 15-20. Manipulation ---")
# 15. Create a new column
df_clean = df_clean.assign(Total_Comp = df_clean['Salary'] + df_clean['Bonus'])

# 16. Rename columns
df_clean = df_clean.rename(columns={'Emp_ID': 'ID', 'Is_Active': 'Active_Status'})

# 17. Drop columns
df_clean = df_clean.drop(columns=['Country'])

# 18. Replace values
df_clean['Active_Status'] = df_clean['Active_Status'].replace({True: 'Yes', False: 'No'})

# 19. Sort values
df_sorted = df_clean.sort_values(by=['Department', 'Salary'], ascending=[True, False])

# 20. Apply a custom function to a column
df_sorted['Tax'] = df_sorted['Salary'].apply(lambda x: x * 0.20 if x > 80000 else x * 0.10)

# 6. Aggregation & Grouping
# -------------------------
print("\n--- 21-25. Aggregation ---")
# 21. Unique values
print("Unique Cities:", df_sorted['City'].unique())
# 22. Count of unique values
print("Number of Departments:", df_sorted['Department'].nunique())
# 23. Value counts (Frequency table)
print("Employees per City:\n", df_sorted['City'].value_counts())

# 24. GroupBy (Split-Apply-Combine)
# Average salary per department
dept_salary = df_sorted.groupby('Department')['Salary'].mean().round(2)
print("\nAverage Salary by Department:\n", dept_salary)

# 25. Multiple aggregations using .agg()
summary = df_sorted.groupby('Department').agg({
    'Salary': ['mean', 'max'],
    'Project_Count': 'sum'
})
print("\nComplex Aggregation:\n", summary)