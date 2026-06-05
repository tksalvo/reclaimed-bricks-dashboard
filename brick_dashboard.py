import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="No16: Reclaimed Bricks", layout="wide")

# HEADER
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

# ====================== DATA ======================
data = { ... }  # (same full data as before - I kept it short here for space)

df = pd.DataFrame(data)

if tier == "free":
    df = df[df["Quarter"].str.contains("2024")].copy()
elif tier == "salvoweb":
    df = df[df["Quarter"].str.contains("2024|2025")].copy()

quarter_order = ["Q3 2024", "Q4 2024", "Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"]
df["Quarter"] = pd.Categorical(df["Quarter"], categories=quarter_order, ordered=True)
df = df.sort_values("Quarter")

# Filters
col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    region = st.selectbox("Select Region", ["US (USD)", "UK (GBP)", "EU (EUR)", "Australia (AUD)"])
with col2:
    price_type = st.radio("Price Display", ["Per Brick", "Per 1,000 Bricks"], horizontal=True)
with col3:
    show_overlay = st.checkbox("Overlay Comparison", value=False)

multiplier = 1000 if price_type == "Per 1,000 Bricks" else 1

# Region map (same as before)
region_map = { ... }  # same as previous version

selected_cols = region_map[region]

st.subheader("Price Trends Over Time")
if show_overlay:
    # Simple overlay example - can be expanded
    st.info("Overlay mode - select multiple regions in future version")
else:
    chart_data = df[["Quarter"] + selected_cols].set_index("Quarter") * multiplier
    st.line_chart(chart_data, use_container_width=True, height=500)

# Export Button
if st.button("📥 Export Current Data as CSV"):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "reclaimed_bricks_data.csv", "text/csv")

st.subheader(f"Current Prices — {region} (Up to {max_year})")
st.dataframe(df[["Quarter"] + selected_cols], use_container_width=True)

# Simple User Submission Form (Trial)
if tier != "free":
    with st.expander("📤 Submit Your Own Price Data (Trial)"):
        st.write("Admin approval required before appearing in median")
        with st.form("submit_data"):
            submitted_region = st.selectbox("Region", ["US", "UK", "EU", "Australia"])
            price = st.number_input("Price per Brick (USD/GBP/etc)", value=1.25)
            brick_type = st.text_input("Brick Type (e.g. Handmade Red)")
            if st.form_submit_button("Submit for Approval"):
                st.success("✅ Data submitted for admin review!")

st.caption("Global Reclaimed Bricks Intelligence • Powered by Grok")