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

# ====================== TIER FROM URL ======================
query_params = st.query_params
tier = query_params.get("tier", ["free"])[0].lower()

# Tier display
if tier == "free":
    st.info("🔓 **Free Tier** — Historical data up to 2024")
    max_year = "2024"
elif tier == "salvoweb":
    st.success("✅ **salvoweb.com Registered User** — Data up to Q4 2025")
    max_year = "2025"
else:  # premium
    st.success("⭐ **Full Marketplace Member** — All data including 2026")
    max_year = "2026"

if st.button("🔑 Login / Register on salvoweb.com"):
    st.markdown("[👉 Go to salvoweb.com](https://salvoweb.com)", unsafe_allow_html=True)

st.markdown("---")

# ====================== CURRENT TIME (West to East) ======================
st.subheader("Current Time (Key Cities)")
time_cols = st.columns(4)

cities = [
    ("Chicago", "America/Chicago"),
    ("London", "Europe/London"),
    ("Brussels", "Europe/Brussels"),
    ("Sydney", "Australia/Sydney")
]

for i, (city, tz) in enumerate(cities):
    with time_cols[i]:
        current = datetime.now(pytz.timezone(tz))
        st.write(f"**{city}**")
        st.write(current.strftime('%H:%M'))   # Only hours and minutes

st.markdown("---")

# ====================== REST OF DASHBOARD ======================
# (Filters, Data, Charts, etc. - keeping the rest the same)
col1, col2 = st.columns([2, 2])

with col1:
    region = st.selectbox("Select Region", ["US (USD)", "UK (GBP)", "EU (EUR)", "Australia (AUD)"])

with col2:
    price_type = st.radio("Price Display", ["Per Brick", "Per 1,000 Bricks"], horizontal=True)

multiplier = 1000 if price_type == "Per 1,000 Bricks" else 1

st.subheader("Price Trends Over Time")
st.line_chart(df.set_index("Quarter"), use_container_width=True, height=450)

st.subheader(f"Current Prices — {region} (Up to {max_year})")

st.subheader("Full Quarterly Data")
st.dataframe(df, use_container_width=True)

st.caption("Global Reclaimed Bricks Intelligence • Powered by Grok")