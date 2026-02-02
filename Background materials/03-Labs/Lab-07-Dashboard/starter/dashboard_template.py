"""
AI Academy Lab 07 - Analytics Dashboard
Starter template (Streamlit)
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page config
st.set_page_config(
    page_title="AI Analytics Dashboard",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI System Analytics Dashboard")
st.markdown("Real-time insights into AI system performance and business value")

# Load data
@st.cache_data
def load_data():
    # TODO: Replace with your data loading logic
    return pd.read_csv("../data/sample_metrics.csv")

df = load_data()

# ============================================
# KPI Cards
# ============================================

st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

# TODO: Calculate and display KPIs
with col1:
    st.metric(
        label="Total Queries",
        value="TODO",
        delta="TODO"
    )

with col2:
    st.metric(
        label="Active Users",
        value="TODO",
        delta="TODO"
    )

with col3:
    st.metric(
        label="Avg Latency",
        value="TODO",
        delta="TODO"
    )

with col4:
    st.metric(
        label="Success Rate",
        value="TODO",
        delta="TODO"
    )

# ============================================
# Charts
# ============================================

st.subheader("📈 Trends")

# TODO: Add line chart for daily queries

# TODO: Add bar chart for latency

# TODO: Add area chart for token usage

# ============================================
# Cost Analysis
# ============================================

st.subheader("💰 Cost & ROI")

# TODO: Calculate costs
# TODO: Show ROI calculation

# ============================================
# Data Table
# ============================================

st.subheader("📋 Raw Data")

if st.checkbox("Show raw data"):
    st.dataframe(df)

# ============================================
# Footer
# ============================================

st.markdown("---")
st.markdown(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
