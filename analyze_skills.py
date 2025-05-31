import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt

# Target skills
target_skills = [
    'sql', 'python', 'r', 'tableau', 'power bi', 'excel', 'vba', 'hadoop',
    'spark', 'pandas', 'numpy', 'machine learning', 'data visualization',
    'statistics', 'aws', 'azure', 'google cloud', 'java', 'c++'
]

df = pd.read_excel("sample_output/indeed_jobs_sample.xlsx")

text = " ".join(df['description'].dropna().astype(str)).lower()

text = re.sub(r"[^\w\s]", " ", text)

# Count of skill mentions
skill_counts = Counter()
for skill in target_skills:
    pattern = r"\b" + re.escape(skill.lower()) + r"\b"
    matches = re.findall(pattern, text)
    skill_counts[skill] = len(matches)

# Display skills
print("\n🔍 Most Mentioned Skills:\n")
for skill, count in skill_counts.most_common():
    print(f"{skill.title():<20} {count}")

# Results
skills, counts = zip(*skill_counts.most_common())
plt.figure(figsize=(10, 6))
bars = plt.bar(skills, counts)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom')

plt.title("Top Skills in Data Analyst Job Descriptions")
plt.ylabel("Mentions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sample_output/skill_bar_chart.png")
plt.show()
