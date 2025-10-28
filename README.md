# 🌍 USGS Earthquake Data Automation Pipeline

## 📘 Overview
This project automates the ingestion, validation, transformation, and visualization of **real-time earthquake data** from the [USGS Earthquake API](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).  
It was developed as part of my **CMCC Data Automation Midterm Project**.

The pipeline retrieves new earthquake data on a schedule, cleans it, saves it for persistence, and generates an **interactive Plotly dashboard** showing magnitudes over time.

---

## ⚙️ Features
- **Automated Ingestion:** Pulls live GeoJSON data from the USGS feed  
- **Data Cleaning:** Filters and normalizes columns before saving  
- **Storage:** Appends results into `data_store.csv` for long-term tracking  
- **Visualization:** Generates `viz/chart.html` — an interactive Plotly chart  
- **Logging:** Every run writes detailed logs in the `logs/` folder  
- **Automation:** Uses CRON (`cron_job.sh`) to schedule recurring runs

---

## 🧠 Project Flow
