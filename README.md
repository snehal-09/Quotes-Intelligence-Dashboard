# Quotes-Intelligence-Dashboard

An **end-to-end Web Scraping, Data Analysis, and Interactive Dashboard project** built using **Python and Streamlit**.
This project scrapes quote and author data from a public website, processes it, and presents insights through a **dynamic, animated, and user-driven UI**.

---

## 🚀 Project Overview

This project demonstrates how to:

* Scrape data from a multi-page website
* Crawl author profile pages
* Clean and structure scraped data
* Perform basic analytics
* Build a **professional interactive dashboard** with Streamlit

🔗 **Data Source**: [https://quotes.toscrape.com](https://quotes.toscrape.com)

---

## ✨ Key Features

### 🔍 Web Scraping & Crawling

* Extracts:

  * Quotes
  * Authors
  * Tags
* Visits individual author profile pages
* Avoids duplicate authors using sets

### 📊 Data Analytics

* Total Quotes, Authors, and Tags
* Top authors by number of quotes
* Most popular author
* Top tags analysis

### 🧠 Smart Analytics (User Input)

Users can type queries like:

* `top 5 authors`
* `most popular author`
* `top tags`
* `top 10 quotes`

The dashboard dynamically responds with charts or tables.

### 🎨 Interactive UI

* Dark / Light mode toggle
* Hover animations on cards
* Smooth fade-in effects
* Clean, modern dashboard layout

### ⬇️ Data Download

* Download scraped data as:

  * CSV
  * Excel (.xlsx)

---

## 🛠️ Tech Stack

* **Python**
* **Requests** – Web requests
* **BeautifulSoup** – HTML parsing
* **Pandas** – Data processing
* **Matplotlib** – Data visualization
* **Streamlit** – Interactive web app
* **OpenPyXL** – Excel export

---

## 📂 Project Structure

```
📁 Quotes-Intelligence-Dashboard
│
├── Quotes_Scrapping.ipynb   # Web scraping notebook
├── app.py                  # Streamlit dashboard
├── quotes_data.csv         # Scraped quotes data
├── authors_data.csv        # Scraped author data
└── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/quotes-intelligence-dashboard.git
cd quotes-intelligence-dashboard
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

The app will open at:
👉 `http://localhost:8501`

---

## 📈 Results

* ✅ 100+ Quotes scraped
* ✅ 50+ Authors extracted
* ✅ Tag-based analysis
* ✅ Clean UTF-8 encoded datasets
* ✅ Fully interactive dashboard

---

## 🧠 What I Learned

* Web scraping and crawling using Python
* Handling pagination and duplicate data
* Data cleaning and preprocessing
* Building dynamic dashboards with Streamlit
* Adding UI animations and theme toggles
* Handling dependencies and deployment readiness

---

## ⚠️ Ethical Note

This project uses a **public practice website** intended for learning web scraping.
No private or restricted data is collected.

---
