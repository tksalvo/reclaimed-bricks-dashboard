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

# ====================== TIER & REGION ======================
query_params = st.query_params
tier = query_params.get("tier", ["free"])[0].lower()

region = st.selectbox("🌍 Select Region / Currency", 
                     ["US (USD)", "UK (GBP)", "EU (EUR)", "Australia (AUD)"])

# Symbol defined VERY EARLY
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

# Current Time
st.subheader("Current Time (Key Cities)")
time_cols = st.columns(4)
cities = [("Chicago", "America/Chicago"), ("London", "Europe/London"), 
          ("Brussels", "Europe/Brussels"), ("Sydney", "Australia/Sydney")]

for i, (city, tz) in enumerate(cities):
    with time_cols[i]:
        current = datetime.now(pytz.timezone(tz))
        st.write(f"**{city}**")
        st.write(current.strftime('%H:%M'))

st.markdown("---")

# Data and rest of the dashboard (shortened for now to test symbol)
st.subheader("Test Section")
st.write(f"**Current Symbol Test:** {symbol}1.25")

st.caption("Currency Symbol Test Version")