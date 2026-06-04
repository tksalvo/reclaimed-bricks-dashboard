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

if tier == "free":
    st.info("🔓 Free Tier — Data up to 2024")
    max_year = "2024"
elif tier == "salvoweb":
    st.success("✅ salvoweb.com User — Data up to Q4 2025")
    max_year = "2025"
else:
    st.success("⭐ Full Marketplace Member — Data up to 2026")
    max_year = "2026"

# Time
st.subheader("Current Time (Key Cities)")
cols = st.columns(4)
cities = [("Chicago", "America/Chicago"), ("London", "Europe/London"), 
          ("Brussels", "Europe/Brussels"), ("Sydney", "Australia/Sydney")]

for i, (city, tz) in enumerate(cities):
    with cols[i]:
        current = datetime.now(pytz.timezone(tz))
        st.write(f"**{city}**")
        st.write(current.strftime('%H:%M'))

# Simple Data
data = {
    "Quarter": ["Q3 2024", "Q4 2024", "Q1 2025", "Q2 2025"],
    "Common_USD": [0.42, 0.44, 0.45, 0.46],
}

df = pd.DataFrame(data)

st.subheader("Price Trends Over Time")
st.line_chart(df.set_index("Quarter"), use_container_width=True, height=400)

st.subheader(f"Current Prices (Up to {max_year})")
st.dataframe(df, use_container_width=True)