import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="No16: Reclaimed Bricks", layout="wide")

st.markdown("### Global OIPRs by Salvo futuREuse Ltd")
st.title("No16: Reclaimed Bricks")

st.caption("""
**Observational Indicative Price Ranges.** Not guaranteed accurate.  
Sourced from Salvo Marketplace members and public websites.  
**Collected by Salvo futuREuse Ltd.**
""")
st.markdown("---")

# Tier
query_params = st.query_params
tier = query_params.get("tier", ["free"])[0].lower()

# Region and Symbol - Defined very early
region = st.selectbox("🌍 Select Region / Currency", 
                     ["UK (GBP)", "US (USD)", "EU (EUR)", "Australia (AUD)"])

symbol = {"US (USD)": "$", "UK (GBP)": "£", "EU (EUR)": "€", "Australia (AUD)": "A$"}[region]

if tier == "free":
    st.info("🔓 Free Tier — Indicative Price Ranges")
    view_mode = "range"
else:
    st.success("⭐ Paid User — Detailed Metrics")
    view_mode = "detailed"

st.markdown("---")

# Test line
st.success(f"Symbol Test → {symbol}1.25")

# Rest of dashboard would go here

st.caption("Test Version - Check if symbols work")