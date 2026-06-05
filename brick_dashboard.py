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

# ====================== TIER ======================
query_params = st.query_params
tier = query_params.get("tier", ["free"])[0].lower()

if tier == "free":
    st.info("🔓 **Free Tier** — Data up to 2024")
    max_year = "2024"
elif tier == "salvoweb":
    st.success("✅ **salvoweb.com Registered User** — Data up to Q4 2025")
    max_year = "2025"
else:
    st.success("⭐ **Full Marketplace Member** — All data including 2026")
    max_year = "2026"

if st.button("🔑 Login / Register on salvoweb.com"):
    st.markdown("[👉 Go to salvoweb.com](https://salvoweb.com)", unsafe_allow_html=True)

st.markdown("---")

# Time
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

# ====================== FULL DATA ======================
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
    "Common_EUR": [0.40, 0.41, 0.42, 0.43, 0.44, 0.45, 0.47, 0.49],
    "Cleaned_EUR": [1.00, 1.03, 1.05, 1.08, 1.10, 1.13, 1.17, 1.20],
    "Premium_EUR": [1.45, 1.48, 1.52, 1.55, 1.60, 1.65, 1.70, 1.75],
    "Antique_EUR": [12.8, 13.0, 13.2, 13.5, 13.8, 14.2, 15.5, 16.2],
    "Common_AUD": [0.68, 0.70, 0.71, 0.73, 0.74, 0.76, 0.78, 0.80],
    "Cleaned_AUD": [1.70, 1.72, 1.75, 1.78, 1.82, 1.85, 1.90, 1.95],
    "Premium_AUD": [2.45, 2.50, 2.55, 2.60, 2.65, 2.70, 2.78, 2.85],
    "Antique_AUD": [21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 25.5, 26.5],
}

df = pd.DataFrame(data)

# Tier filtering
if tier == "free":
    df = df[df["Quarter"].str.contains("2024")].copy()
elif tier == "salvoweb":
    df = df[df["Quarter"].str.contains("2024|2025")].copy()

# ====================== FILTERS ======================
col1, col2 = st.columns([2, 2])
with col1:
    region = st.selectbox("Select Region / Currency", 
                         ["US (USD)", "UK (GBP)", "EU (EUR)", "Australia (AUD)"])
with col2:
    price_type = st.radio("Price Display", ["Per Brick", "Per 1,000 Bricks"], horizontal=True)

multiplier = 1000 if price_type == "Per 1,000 Bricks" else 1

# ====================== CHART ======================
st.subheader("Price Trends Over Time")

region_map = {
    "US (USD)": ["Common_USD", "Cleaned_USD", "Premium_USD", "Antique_USD"],
    "UK (GBP)": ["Common_GBP", "Cleaned_GBP", "Premium_GBP", "Antique_GBP"],
    "EU (EUR)": ["Common_EUR", "Cleaned_EUR", "Premium_EUR", "Antique_EUR"],
    "Australia (AUD)": ["Common_AUD", "Cleaned_AUD", "Premium_AUD", "Antique_AUD"],
}

selected_cols = region_map[region]
chart_data = df[["Quarter"] + selected_cols].set_index("Quarter") * multiplier

st.line_chart(chart_data, use_container_width=True, height=500)

st.subheader(f"Current Prices — {region} (Up to {max_year})")
st.dataframe(df[["Quarter"] + selected_cols], use_container_width=True)

st.caption("Global Reclaimed Bricks Intelligence • Powered by Grok")