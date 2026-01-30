import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# Load data
df = pd.read_csv("cleaned_telco_churn.csv")

# Title
st.title("Customer Churn Analysis Dashboard")
st.markdown("Analyze customer churn patterns and key business drivers.")

# Sidebar filters
st.sidebar.header("Filters")

contract_filter = st.sidebar.multiselect(
    "Select Contract Type",
    options=df["Contract"].unique(),
    default=df["Contract"].unique()
)

internet_filter = st.sidebar.multiselect(
    "Select Internet Service",
    options=df["InternetService"].unique(),
    default=df["InternetService"].unique()
)

filtered_df = df[
    (df["Contract"].isin(contract_filter)) &
    (df["InternetService"].isin(internet_filter))
]

# KPIs
total_customers = filtered_df.shape[0]
churn_rate = round(filtered_df["Churn"].mean() * 100, 2)
avg_monthly = round(filtered_df["MonthlyCharges"].mean(), 2)
avg_tenure = round(filtered_df["tenure"].mean(), 1)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate (%)", churn_rate)
col3.metric("Avg Monthly Charges", avg_monthly)
col4.metric("Avg Tenure (Months)", avg_tenure)

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        filtered_df,
        x="Contract",
        y="Churn",
        title="Churn Rate by Contract Type",
        color="Contract"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.box(
        filtered_df,
        x="Churn",
        y="MonthlyCharges",
        title="Monthly Charges vs Churn",
        color="Churn"
    )
    st.plotly_chart(fig2, use_container_width=True)

# Tenure group analysis
filtered_df["tenure_group"] = pd.cut(
    filtered_df["tenure"],
    bins=[0, 12, 24, 36, 48, 60, 72],
    labels=["0-1 yr", "1-2 yrs", "2-3 yrs", "3-4 yrs", "4-5 yrs", "5+ yrs"]
)

fig3 = px.bar(
    filtered_df,
    x="tenure_group",
    y="Churn",
    title="Churn Rate by Tenure Group"
)

st.plotly_chart(fig3, use_container_width=True)

# Insights section
st.markdown("## Key Insights")
st.write("""
- Customers on **month-to-month contracts** show the highest churn.
- **Early-tenure customers** are most at risk.
- Higher **monthly charges** are associated with increased churn.
""")
