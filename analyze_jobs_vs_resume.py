import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load job data
df = pd.read_excel("sample_output/indeed_jobs_sample.xlsx")

# Drop rows without descriptions
df = df.dropna(subset=["description"])

# Combine job title + description for better matching
df["combined_text"] = df["positionName"].fillna('') + " " + df["description"]

# Resume text
resume_text = """
Data analyst with experience in business intelligence, fraud prevention, and customer success analytics.
Skilled in Python, SQL, Excel, Tableau, and Power BI. Projects include job scrapers, fraud detection models,
and dashboards using Python, pandas, scikit-learn, matplotlib, and Excel.
"""

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["combined_text"])
resume_vec = vectorizer.transform([resume_text])

# Compute similarity
df["similarity_score"] = cosine_similarity(tfidf_matrix, resume_vec).flatten()

# Sort by similarity
top_matches = df.sort_values(by="similarity_score", ascending=False).head(10)

# Save to Excel
top_matches.to_excel("output/top_matches_resume_based.xlsx", index=False)
print("✅ Top matching jobs saved to output/top_matches_resume_based.xlsx")
