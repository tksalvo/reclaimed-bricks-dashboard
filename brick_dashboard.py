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

# Login button
if st.button("🔑 Login / Register on salvoweb.com"):
    st.markdown("[👉 Go to salvoweb.com](https://salvoweb.com)", unsafe_allow_html=True)

st.markdown("---")

# ====================== CURRENT TIME ======================
st.subheader("Current Time (Key Cities)")
time_cols = st.columns(4)
cities = [("Sydney", "Australia/Sydney"), ("Brussels", "Europe/Brussels"),
          ("London", "Europe/London"), ("Chicago", "America/Chicago")]

for i, (city, tz) in enumerate(cities):
    with time_cols[i]:
        current = datetime.now(pytz.timezone(tz))
        st.write(f"**{city}**")
        st.write(current.strftime('%Y-%m-%d %H:%M'))

st.markdown("---")

# ====================== DATA ======================
data = {
    "Quarter": ["Q3 2024", "Q4 2024", "Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"],
    "Common_USD": [0.42, 0.44, 0.45, 0.46, 0.47, 0.48, 0.50, 0.525],
    "Cleaned_USD": [1.05, 1.08, 1.10, 1.12, 1.15, 1.18, 1.22, 1.275],
    "Premium_USD": [1.50, 1.55, 1.58, 1.62, 1.67, 1.72, 1.78, 1.85],
    "Antique_USD": [13.5, 13.8, 14.0, 14.2, 14.5, 14.8, 16.0, 17.5],
    "Common_GBP": [0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.41],
    "Cleaned_GBP": [0.85, 0.86, 0.88, 0.90, 0.92, 0.95, 0.97, 1.00],
    "Premium_GBP": [1.20, 1.22, 1.25, 1.28, 1.30, 1.35, 1.40, 1.45],
    "Antique_GBP": [10.5, 10.8, 11.0, 11.2, 11.3, 11.5, 12.5, 13.7],
    # Add EU and AUD columns as needed
}

df = pd.DataFrame(data)

# Filter data based on tier
if tier == "free":
    df = df[df["Quarter"].str.contains("2024")].copy()
elif tier == "salvoweb":
    df = df[df["Quarter"].str.contains("2024|2025")].copy()

# ====================== FILTERS ======================
col1, col2 = st.columns([2, 2])

with col1:
    region = st.selectbox("Select Region", ["US (USD)", "UK (GBP)", "EU (EUR)", "Australia (AUD)"])

with col2:
    price_type = st.radio("Price Display", ["Per Brick", "Per 1,000 Bricks"], horizontal=True)

multiplier = 1000 if price_type == "Per 1,000 Bricks" else 1

# Chart (simplified)
st.subheader("Price Trends Over Time")
st.line_chart(df.set_index("Quarter"), use_container_width=True, height=450)

# Current Prices
st.subheader(f"Current Prices — {region} (Up to {max_year})")

st.subheader("Full Quarterly Data")
st.dataframe(df, use_container_width=True)

st.caption("Global Reclaimed Bricks Intelligence • Powered by Grok")