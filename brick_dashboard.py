import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Reclaimed Bricks Dashboard", layout="wide")
st.title("🧱 Reclaimed Bricks Market Benchmark Dashboard")
st.markdown(f"**Last Updated:** {datetime.now().strftime('%B %d, %Y')}")

# ====================== DATA ======================
data = {
    "Quarter": ["Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"],
    "Common_USD": [0.45, 0.475, 0.50, 0.525],
    "Cleaned_USD": [1.125, 1.15, 1.20, 1.275],
    "Premium_USD": [1.625, 1.70, 1.775, 1.85],
    "Antique_USD": [14.5, 14.5, 16.5, 17.5],
    "Common_GBP": [0.35, 0.37, 0.39, 0.41],
    "Cleaned_GBP": [0.88, 0.90, 0.94, 1.00],
    "Premium_GBP": [1.27, 1.33, 1.39, 1.45],
    "Antique_GBP": [11.3, 11.3, 12.9, 13.7],
}

df = pd.DataFrame(data)

# ====================== FILTERS ======================
col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    region = st.selectbox("Region", ["Both (USD & GBP)", "US Only (USD)", "UK Only (GBP)"])

with col2:
    price_type = st.radio("Price Display", ["Per Brick", "Per 1,000 Bricks"], horizontal=True)

with col3:
    st.write("")  # Spacer

# ====================== CHARTS ======================
st.subheader("Price Trends Over Time")

if price_type == "Per Brick":
    multiplier = 1
    unit = "per brick"
else:
    multiplier = 1000
    unit = "per 1,000 bricks"

# Filter columns based on region
if region == "US Only (USD)":
    cols = ["Common_USD", "Cleaned_USD", "Premium_USD", "Antique_USD"]
    labels = ["Common", "Cleaned", "Premium", "Antique"]
elif region == "UK Only (GBP)":
    cols = ["Common_GBP", "Cleaned_GBP", "Premium_GBP", "Antique_GBP"]
    labels = ["Common", "Cleaned", "Premium", "Antique"]
else:
    cols = ["Common_USD", "Cleaned_USD", "Premium_USD", "Antique_USD"]
    labels = ["Common (USD)", "Cleaned (USD)", "Premium (USD)", "Antique (USD)"]

chart_data = df[["Quarter"] + cols].set_index("Quarter") * multiplier

st.line_chart(chart_data, use_container_width=True, height=520)

# ====================== CURRENT PRICES ======================
st.subheader("Current Prices (Q2 2026)")

current = df.iloc[-1]

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Common", f"${current['Common_USD']*multiplier:.2f}" if "USD" in region or region == "Both" else f"£{current['Common_GBP']*multiplier:.2f}")
with c2:
    st.metric("Cleaned / Graded", f"${current['Cleaned_USD']*multiplier:.2f}" if "USD" in region or region == "Both" else f"£{current['Cleaned_GBP']*multiplier:.2f}")
with c3:
    st.metric("Premium / Heritage", f"${current['Premium_USD']*multiplier:.2f}" if "USD" in region or region == "Both" else f"£{current['Premium_GBP']*multiplier:.2f}")
with c4:
    st.metric("Antique / Rare", f"${current['Antique_USD']*multiplier:.1f}" if "USD" in region or region == "Both" else f"£{current['Antique_GBP']*multiplier:.1f}")

# Full Data Table
st.subheader("Full Quarterly Data")
st.dataframe(df, use_container_width=True)

st.caption("Reclaimed Bricks Marketplace Intelligence • Built with Grok")