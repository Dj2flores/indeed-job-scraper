import os
import requests
import pandas as pd

# Create folder if it doesn't exist
os.makedirs("sample_output", exist_ok=True)

url = "https://api.apify.com/v2/datasets/BMmrW6MBTZoYlvwR5/items?clean=true&format=json&limit=1000"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
df.to_excel("sample_output/indeed_jobs_sample.xlsx", index=False)

print(f"✅ Success! {len(df)} jobs saved to sample_output/indeed_jobs_sample.xlsx")
