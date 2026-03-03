import pandas as pd
import requests

# Step 1: Create sample law firm data (this is our "input")
firms = [
    {"firm_name": "Smith & Associates", "city": "New York", "size": "mid-size", "practice_area": "Corporate Law"},
    {"firm_name": "Johnson Legal Group", "city": "Chicago", "size": "mid-size", "practice_area": "Litigation"},
    {"firm_name": "Pacific Law Partners", "city": "San Francisco", "size": "mid-size", "practice_area": "IP Law"},
    {"firm_name": "Texas Legal Solutions", "city": "Austin", "size": "small", "practice_area": "Family Law"},
    {"firm_name": "Eastern Advocates", "city": "Boston", "size": "mid-size", "practice_area": "Employment Law"},
]

# Step 2: Convert to a DataFrame (like a spreadsheet in Python)
df = pd.DataFrame(firms)

# Step 3: Add a basic ICP score (Ideal Customer Profile)
# August targets mid-size firms, so we score them
def score_firm(row):
    score = 0
    if row["size"] == "mid-size":
        score += 50
    if row["practice_area"] in ["Corporate Law", "IP Law", "Employment Law"]:
        score += 30
    if row["city"] in ["New York", "San Francisco", "Chicago"]:
        score += 20
    return score

df["icp_score"] = df.apply(score_firm, axis=1)

# Step 4: Sort by score (best leads first)
df = df.sort_values("icp_score", ascending=False)

# Step 5: Export to CSV
df.to_csv("enriched_firms.csv", index=False)

print("Pipeline complete!")
print(df)