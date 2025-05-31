# 📊 Indeed Job Scraper (Apify + Python)

This project uses [Apify](https://apify.com/) to scrape Data Analyst job postings from [Indeed](https://indeed.com), then pulls the results via API using Python and exports the data to Excel. It's ideal for portfolio use, job trend analysis, or skill extraction from real job listings.

---

## 📊 Skill Frequency Chart
This chart visualizes the most commonly mentioned skills found in Data Analyst job descriptions scraped from Indeed using Apify. It shows demand for tools like SQL, Python, Excel, and BI platforms across California listings.

---

## 🚀 Features

- ✅ Scrapes jobs by keyword and location using Apify cloud actor
- ✅ Pulls job data via Apify Dataset API
- ✅ Saves job listings to Excel (`.xlsx`)
- ✅ Easy to automate and customize
- ✅ Can be used for dashboards or job market analysis

---

## 🧠 Use Case

This tool is perfect for:
- Aspiring data analysts tracking job opportunities
- Resume tailoring based on skills in demand
- Portfolio visualizations using real-world data

---

## 🛠 How It Works

1. Configure and run the [`misceres/indeed-scraper`](https://apify.com/misceres/indeed-scraper) actor on Apify
2. Get the API URL of the dataset output (format: `format=json`)
3. Paste the URL into `fetch_apify_jobs.py`
4. Run the script to download job listings and save them to `sample_output/indeed_jobs_sample.xlsx`

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

## 🧪 How to Run

```bash
pip install -r requirements.txt
python fetch_apify_jobs.py

---

## Requirements / Data Source

Python 3.8+
pandas
requests
openpyxl

Data Source

Apify Indeed Scraper
Indeed.com