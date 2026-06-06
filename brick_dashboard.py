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

# Region Selector + Symbol
region = st.selectbox("🌍 Select Region / Currency", 
                     ["US (USD)", "UK (GBP)", "EU (EUR)", "Australia (AUD)"])

symbol = {"US (USD)": "$", "UK (GBP)": "£", "EU (EUR)": "€", "Australia (AUD)": "A$"}[region]

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

# Data (simplified for testing)
quarters = ["Q3 2024", "Q4 2024", "Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"]
brick_types = ["Handmade"]*8 + ["Wirecut"]*8 + ["Pressed"]*8

data = {
    "Quarter": quarters * 3,
    "Type": brick_types,
    "Common_USD": [0.55]*8 + [0.38]*8 + [0.48]*8,
    "Cleaned_USD": [1.35]*8 + [0.95]*8 + [1.10]*8,
    "Premium_USD": [2.10]*8 + [1.45]*8 + [1.75]*8,
    "Common_GBP": [0.42]*8 + [0.30]*8 + [0.38]*8,
    "Cleaned_GBP": [1.05]*8 + [0.75]*8 + [0.88]*8,
    "Premium_GBP": [1.65]*8 + [1.15]*8 + [1.40]*8,
    "Common_EUR": [0.40]*8 + [0.29]*8 + [0.36]*8,
    "Cleaned_EUR": [1.00]*8 + [0.72]*8 + [0.85]*8,
    "Premium_EUR": [1.55]*8 + [1.10]*8 + [1.32]*8,
    "Common_AUD": [0.68]*8 + [0.48]*8 + [0.58]*8,
    "Cleaned_AUD": [1.70]*8 + [1.20]*8 + [1.40]*8,
    "Premium_AUD": [2.45]*8 + [1.75]*8 + [2.05]*8,
}

df = pd.DataFrame(data)

# Tier filtering
if tier == "free":
    df = df[df["Quarter"].str.contains("2024")].copy()
elif tier == "salvoweb":
    df = df[df["Quarter"].str.contains("2024|2025")].copy()

# Sort
quarter_order = ["Q3 2024", "Q4 2024", "Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"]
df["Quarter"] = pd.Categorical(df["Quarter"], categories=quarter_order, ordered=True)
df = df.sort_values("Quarter")

# Tabs
tab1, tab2, tab3 = st.tabs(["🧱 Handmade", "🔨 Wirecut", "🪨 Pressed"])

region_map = {"US (USD)": "USD", "UK (GBP)": "GBP", "EU (EUR)": "EUR", "Australia (AUD)": "AUD"}
curr = region_map[region]

for tab, brick_type in zip([tab1, tab2, tab3], ["Handmade", "Wirecut", "Pressed"]):
    with tab:
        st.subheader(f"{brick_type} Bricks — {region}")
        type_df = df[df["Type"] == brick_type]
        
        cols = [f"Common_{curr}", f"Cleaned_{curr}", f"Premium_{curr}"]
        
        if view_mode == "range":
            st.metric("Common", f"{symbol}{type_df[cols[0]].min():.2f} – {symbol}{type_df[cols[0]].max():.2f}")
            st.metric("Cleaned", f"{symbol}{type_df[cols[1]].min():.2f} – {symbol}{type_df[cols[1]].max():.2f}")
            st.metric("Premium", f"{symbol}{type_df[cols[2]].min():.2f} – {symbol}{type_df[cols[2]].max():.2f}")
        else:
            st.metric("Median", f"{symbol}{type_df[cols[1]].median():.2f}")
            st.metric("Last Reported", f"{symbol}{type_df[cols[1]].iloc[-1]:.2f}")
            st.metric("Weighted Avg", f"{symbol}{type_df[cols[1]].mean():.2f}")

        chart_data = type_df[["Quarter"] + cols].set_index("Quarter")
        st.line_chart(chart_data, use_container_width=True, height=450)

st.caption("Global Reclaimed Bricks Intelligence • Powered by Grok")