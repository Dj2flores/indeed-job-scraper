import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt

# Define your list of target skills
target_skills = [
    'sql', 'python', 'r', 'tableau', 'power bi', 'excel', 'vba', 'hadoop',
    'spark', 'pandas', 'numpy', 'machine learning', 'data visualization',
    'statistics', 'aws', 'azure', 'google cloud', 'java', 'c++'
]

# Load the Excel file
df = pd.read_excel("sample_output/indeed_jobs_sample.xlsx")

# Combine all descriptions into one big string
text = " ".join(df['description'].dropna().astype(str)).lower()

# Clean text (remove punctuation)
text = re.sub(r"[^\w\s]", " ", text)

# Count skill mentions manually
skill_counts = Counter()
for skill in target_skills:
    pattern = r"\b" + re.escape(skill.lower()) + r"\b"
    matches = re.findall(pattern, text)
    skill_counts[skill] = len(matches)

# Display top skills
print("\n🔍 Most Mentioned Skills:\n")
for skill, count in skill_counts.most_common():
    print(f"{skill.title():<20} {count}")

# Plot results
skills, counts = zip(*skill_counts.most_common())
plt.figure(figsize=(10, 6))
plt.bar(skills, counts)
plt.title("Top Skills in Data Analyst Job Descriptions")
plt.ylabel("Mentions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

