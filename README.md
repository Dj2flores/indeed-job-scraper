# 🧠 Indeed Job Scraper and Resume-Based Job Match Analyzer

This project scrapes job postings from Indeed using the Apify API, analyzes the most mentioned skills using NLP, and compares the scraped jobs against my resume to recommend the best matches.

---

## 📊 Skill Frequency Chart
This chart visualizes the most commonly mentioned skills found in Data Analyst job descriptions scraped from Indeed using Apify. It shows demand for tools like SQL, Python, Excel, and BI platforms across California listings.
![Skills](https://github.com/user-attachments/assets/b72c1cb9-9417-4139-abd7-161df0a398a0)

---

## 📦 Features

  - 🔍 Scrapes job data (title, company, location, description, date)
  - 📊 Analyzes common skills using Natural Language Processing (NLP)
  - ✅ Matches top jobs to your resume using TF-IDF and cosine similarity
  - 📈 Visualizes top-mentioned skills and top job recommendations

---

## 🧠 Use Case

This tool is perfect for:
  - Aspiring data analysts tracking job opportunities
  - Resume tailoring based on skills in demand
  - Portfolio visualizations using real-world data

---

## 📊 Skill Frequency Chart
This chart visualizes the most commonly mentioned skills found in Data Analyst job descriptions scraped from Indeed using Apify. It shows demand for tools like SQL, Python, Excel, and BI platforms across California listings.

### Top Mentioned Skills
![Skills](https://github.com/user-attachments/assets/b72c1cb9-9417-4139-abd7-161df0a398a0)

### Top Job Matches Based on my Resume Similarity
![Top 10 Matches](https://github.com/user-attachments/assets/2f7a7849-58d8-4d71-96d0-054404d3f73f)

---
## 📊 Resume-Based Job Matches (Summary)

### Top Job Titles
***Senior Data Analyst
***Business Intelligence Analyst
***Bank Fraud Senior Business Analyst
***Data Analyst with Project Controls

### Top Companies
***Disney
***Crowe LLP
***GT’S Living Foods
***Brio Solutions LLC

### Highest Match Score
***~0.40 (Crowe LLP – Bank Fraud Senior Business Analyst)

### Job Locations
***Primarily in Los Angeles and Santa Monica

### Salary Ranges
***Vary from ~$85,000 to over $218,000/year depending on role

---

## 📁 Output

**File:** `sample_output/indeed_jobs_sample.xlsx`

**Fields:**
- `title`: Job title (e.g., "Data Analyst")
- `company`: Hiring company
- `location`: Job location (e.g., San Francisco, Remote)
- `description`: Summary of job responsibilities
- `posted date`: How recently the job was posted

---
## Requirements / Data Source

- Python 3.8+
- pandas
- requests
- openpyxl

Data Source

- Apify Indeed Scraper
- Indeed.com


## 🧪 How to Run

```bash
pip install -r requirements.txt
python fetch_apify_jobs.py
