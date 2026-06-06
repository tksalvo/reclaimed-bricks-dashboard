import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="No16: Reclaimed Bricks", layout="wide")

# ====================== HEADER ======================
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

# Region selector - GBP first as you suggested
region = st.selectbox("🌍 Select Region / Currency", 
                     ["UK (GBP)", "US (USD)", "EU (EUR)", "Australia (AUD)"])

# Symbol mapping
symbol = {"US (USD)": "$", "UK (GBP)": "£", "EU (EUR)": "€", "Australia (AUD)": "A$"}[region]

if tier == "free":
    st.info("🔓 **Free Tier** — Indicative Price Ranges (up to 2024)")
    view_mode = "range"
elif tier == "salvoweb":
    st.success("✅ **salvoweb.com Registered User** — Enhanced Data up to Q4 2025")
    view_mode = "detailed"
else:
    st.success("⭐ **Full Marketplace Member** — Full Analytics including 2026")
    view_mode = "detailed"

if st.button("🔑 Login / Register on salvoweb.com"):
    st.markdown("[👉 Go to salvoweb.com](https://salvoweb.com)", unsafe_allow_html=True)

st.markdown("---")

# Test line to see symbol
st.success(f"Selected Region: {region} → Symbol: **{symbol}**")

# Rest of dashboard (time, tabs, etc.) can be added later

st.caption("Currency Symbol Test Version")