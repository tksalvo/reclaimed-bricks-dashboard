import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Reclaimed Bricks Dashboard", layout="wide")

st.title("🧱 Reclaimed Bricks Market Benchmark Dashboard")
st.markdown(f"**Last Updated:** {datetime.now().strftime('%B %d, %Y')}")

# Sample Data
data = {
    "Quarter": ["Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"],
    "Common_Mid": [0.45, 0.475, 0.50, 0.525],
    "Cleaned_Mid": [1.125, 1.15, 1.20, 1.275],
    "Premium_Mid": [1.625, 1.70, 1.775, 1.85],
    "Antique_Mid": [14.5, 14.5, 16.5, 17.5],
}

df = pd.DataFrame(data)

# Layout
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("Price Trends Over Time (per brick)")

    # Simple line chart using Streamlit native
    st.line_chart(
        df.set_index("Quarter")[["Common_Mid", "Cleaned_Mid", "Premium_Mid", "Antique_Mid"]],
        use_container_width=True,
        height=500
    )

with col2:
    st.subheader("Current Prices (Q2 2026)")
    current = df.iloc[-1]
    st.metric("Common", f"${current['Common_Mid']:.2f}")
    st.metric("Cleaned/Graded", f"${current['Cleaned_Mid']:.2f}")
    st.metric("Premium/Heritage", f"${current['Premium_Mid']:.2f}")
    st.metric("Antique/Rare", f"${current['Antique_Mid']:.1f}")

st.subheader("Full Quarterly Data")
st.dataframe(df, use_container_width=True)

st.caption("Reclaimed Bricks Marketplace Intelligence • Powered by Grok")