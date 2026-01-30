# Customer Churn Analysis Dashboard

## Problem Statement
Customer churn is a major challenge for subscription-based businesses, directly impacting revenue and growth. This project analyzes telecom customer data to identify key factors that contribute to churn and presents insights through an interactive dashboard for business decision-making.

## Project Overview
This project focuses on understanding customer churn behavior using a real-world telecom dataset. The workflow includes data cleaning, exploratory data analysis, and the development of an interactive dashboard that allows users to explore churn patterns dynamically.

The dashboard is designed to help stakeholders identify high-risk customer segments and understand the business drivers behind churn.

## Tools and Technologies
- Python
- Pandas and NumPy for data manipulation
- Matplotlib and Seaborn for exploratory analysis
- Plotly for interactive visualizations
- Streamlit for dashboard development

## Dataset
The dataset used in this project is the Telco Customer Churn dataset sourced from Kaggle. It contains customer demographic information, account details, service usage, and churn status.

## Key Analysis Steps
- Data cleaning and preprocessing
- Handling missing values and data type conversions
- Exploratory data analysis to identify churn patterns
- Feature grouping for tenure-based analysis
- KPI calculation for business insights

## Key Insights
- Customers on month-to-month contracts have the highest churn rate.
- Customers within their first year of service are more likely to churn.
- Higher monthly charges are associated with increased churn.
- Fiber optic internet service users show higher churn compared to DSL users.

## Dashboard Features
- High-level KPIs including total customers, churn rate, average monthly charges, and average tenure
- Interactive filters for contract type and internet service
- Visual analysis of churn by contract, tenure group, and monthly charges
- Summary of key business insights

## How to Run the Project Locally
1. Clone the repository
2. Install the required dependencies
   ```bash
   pip install -r requirements.txt
   Run the Streamlit application

streamlit run app.py
