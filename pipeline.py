import pandas as pd

# Step 1: Read from external CSV file
print("Reading firms from CSV...")
df = pd.read_csv("firms_input.csv")
print(f"Loaded {len(df)} firms")

# Step 2: ICP scoring function
def score_firm(row):
    score = 0
    if row["size"] == "mid-size":
        score += 50
    if row["practice_area"] in ["Corporate Law", "IP Law", "Employment Law"]:
        score += 30
    if row["city"] in ["New York", "San Francisco", "Chicago", "Boston", "Washington DC"]:
        score += 20
    return score

# Step 3: Apply score to every row
df["icp_score"] = df.apply(score_firm, axis=1)

# Step 4: Add priority label
def label_priority(score):
    if score >= 90:
        return "High Priority"
    elif score >= 50:
        return "Medium Priority"
    else:
        return "Low Priority"

df["priority"] = df["icp_score"].apply(label_priority)

# Step 5: Sort best leads first
df = df.sort_values("icp_score", ascending=False)

# Step 6: Export enriched output
df.to_csv("enriched_firms.csv", index=False)

print("\nPipeline complete! Results:")
print(df[["firm_name", "city", "icp_score", "priority"]])