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

# ====================== DATA (with Brick Types) ======================
quarters = ["Q3 2024", "Q4 2024", "Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"]

data = {
    "Quarter": quarters * 3,
    "Type": ["Handmade"]*8 + ["Wirecut"]*8 + ["Pressed"]*8,
    "Common_USD": [0.55,0.57,0.58,0.60,0.62,0.64,0.66,0.68] + [0.38,0.40,0.41,0.42,0.43,0.44,0.45,0.47] + [0.48,0.50,0.51,0.52,0.53,0.55,0.57,0.59],
    "Cleaned_USD": [1.35,1.38,1.42,1.45,1.48,1.52,1.55,1.60] + [0.95,0.98,1.00,1.03,1.05,1.08,1.12,1.15] + [1.10,1.13,1.16,1.20,1.23,1.27,1.30,1.35],
    "Premium_USD": [2.10,2.15,2.20,2.25,2.30,2.35,2.42,2.50] + [1.45,1.48,1.52,1.55,1.60,1.65,1.70,1.75] + [1.75,1.80,1.85,1.90,1.95,2.00,2.05,2.10],
}

df = pd.DataFrame(data)

# Tier filtering
if tier == "free":
    df = df[df["Quarter"].str.contains("2024")].copy()
elif tier == "salvoweb":
    df = df[df["Quarter"].str.contains("2024|2025")].copy()

# Chronological order
quarter_order = ["Q3 2024", "Q4 2024", "Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"]
df["Quarter"] = pd.Categorical(df["Quarter"], categories=quarter_order, ordered=True)
df = df.sort_values("Quarter")

# ====================== TABS ======================
tab1, tab2, tab3 = st.tabs(["Handmade", "Wirecut", "Pressed"])

with tab1:
    st.subheader("Handmade Bricks")
    type_df = df[df["Type"] == "Handmade"]
    st.line_chart(type_df.set_index("Quarter")[["Common_USD", "Cleaned_USD", "Premium_USD"]], height=450)

with tab2:
    st.subheader("Wirecut Bricks")
    type_df = df[df["Type"] == "Wirecut"]
    st.line_chart(type_df.set_index("Quarter")[["Common_USD", "Cleaned_USD", "Premium_USD"]], height=450)

with tab3:
    st.subheader("Pressed Bricks")
    type_df = df[df["Type"] == "Pressed"]
    st.line_chart(type_df.set_index("Quarter")[["Common_USD", "Cleaned_USD", "Premium_USD"]], height=450)

# Export
if st.button("📥 Export Current View as CSV"):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "reclaimed_bricks_data.csv", "text/csv")

st.caption("Global Reclaimed Bricks Intelligence • Powered by Grok")