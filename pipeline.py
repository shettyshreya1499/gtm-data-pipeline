import pandas as pd
import requests
import time

# Your Hunter.io API key
HUNTER_API_KEY = "48c0479609e00c94ff74956ab2f5a3db56a9aabe"

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

# Step 3: Apply score
df["icp_score"] = df.apply(score_firm, axis=1)

# Step 4: Priority label
def label_priority(score):
    if score >= 90:
        return "High Priority"
    elif score >= 50:
        return "Medium Priority"
    else:
        return "Low Priority"

df["priority"] = df["icp_score"].apply(label_priority)

# Step 5: Enrich with Hunter.io API
def enrich_with_hunter(domain):
    try:
        url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
        response = requests.get(url)
        data = response.json()
        
        emails_found = data["data"]["emails"]
        email_count = len(emails_found)
        pattern = data["data"]["pattern"] or "unknown"
        
        print(f"  {domain}: {email_count} emails found, pattern: {pattern}")
        return email_count, pattern
    except Exception as e:
        print(f"  {domain}: API error - {e}")
        return 0, "unknown"

print("\nEnriching firms with Hunter.io...")
email_counts = []
email_patterns = []

for domain in df["website"]:
    count, pattern = enrich_with_hunter(domain)
    email_counts.append(count)
    email_patterns.append(pattern)
    time.sleep(0.5)  # Be polite to the API

df["emails_found"] = email_counts
df["email_pattern"] = email_patterns

# Step 6: Sort best leads first
df = df.sort_values("icp_score", ascending=False)

# Step 7: Export
df.to_csv("enriched_firms.csv", index=False)

print("\nPipeline complete! Results:")
print(df[["firm_name", "icp_score", "priority", "emails_found", "email_pattern"]])