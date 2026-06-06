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
                     ["UK (GBP)", "US (USD)", "EU (EUR)", "Australia (AUD)"])

# Force symbol definition
if region == "US (USD)":
    symbol = "$"
elif region == "UK (GBP)":
    symbol = "£"
elif region == "EU (EUR)":
    symbol = "€"
else:
    symbol = "A$"

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

# Data + Tabs (using the previous full data structure)
# ... (keep your full data here)

st.caption("Global Reclaimed Brimport streamlit as st
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

# ====================== REGION & SYMBOL (Explicit) ======================
region = st.selectbox("🌍 Select Region / Currency", 
                     ["UK (GBP)", "US (USD)", "EU (EUR)", "Australia (AUD)"])

if region == "US (USD)":
    symbol = "$"
elif region == "UK (GBP)":
    symbol = "£"
elif region == "EU (EUR)":
    symbol = "€"
else:
    symbol = "A$"

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

# ====================== DATA ======================
quarters = ["Q3 2024", "Q4 2024", "Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"]
brick_types = ["Handmade"]*8 + ["Wirecut"]*8 + ["Pressed"]*8

data = {
    "Quarter": quarters * 3,
    "Type": brick_types,
    "Common_USD": [0.55,0.57,0.58,0.60,0.62,0.64,0.66,0.68] + [0.38,0.40,0.41,0.42,0.43,0.44,0.45,0.47] + [0.48,0.50,0.51,0.52,0.53,0.55,0.57,0.59],
    "Cleaned_USD": [1.35,1.38,1.42,1.45,1.48,1.52,1.55,1.60] + [0.95,0.98,1.00,1.03,1.05,1.08,1.12,1.15] + [1.10,1.13,1.16,1.20,1.23,1.27,1.30,1.35],
    "Premium_USD": [2.10,2.15,2.20,2.25,2.30,2.35,2.42,2.50] + [1.45,1.48,1.52,1.55,1.60,1.65,1.70,1.75] + [1.75,1.80,1.85,1.90,1.95,2.00,2.05,2.10],
    "Common_GBP": [0.42,0.44,0.45,0.46,0.47,0.48,0.50,0.52] + [0.30,0.32,0.33,0.34,0.35,0.36,0.37,0.38] + [0.38,0.39,0.40,0.41,0.42,0.43,0.44,0.46],
    "Cleaned_GBP": [1.05,1.08,1.10,1.12,1.15,1.18,1.22,1.25] + [0.75,0.78,0.80,0.82,0.85,0.88,0.90,0.92] + [0.88,0.90,0.92,0.95,0.97,1.00,1.02,1.05],
    "Premium_GBP": [1.65,1.70,1.75,1.80,1.85,1.90,1.95,2.00] + [1.15,1.18,1.20,1.23,1.27,1.30,1.35,1.40] + [1.40,1.42,1.45,1.48,1.52,1.55,1.60,1.65],
    "Common_EUR": [0.40,0.41,0.42,0.43,0.44,0.45,0.47,0.49] + [0.29,0.30,0.31,0.32,0.33,0.34,0.35,0.36] + [0.36,0.37,0.38,0.39,0.40,0.41,0.42,0.44],
    "Cleaned_EUR": [1.00,1.03,1.05,1.08,1.10,1.13,1.17,1.20] + [0.72,0.74,0.76,0.78,0.80,0.82,0.85,0.88] + [0.85,0.87,0.90,0.92,0.95,0.97,1.00,1.03],
    "Premium_EUR": [1.55,1.60,1.65,1.70,1.75,1.80,1.85,1.90] + [1.10,1.13,1.15,1.18,1.22,1.25,1.30,1.35] + [1.32,1.35,1.38,1.42,1.45,1.48,1.52,1.58],
    "Common_AUD": [0.68,0.70,0.71,0.73,0.74,0.76,0.78,0.80] + [0.48,0.50,0.51,0.52,0.53,0.55,0.56,0.58] + [0.58,0.60,0.61,0.62,0.64,0.66,0.68,0.70],
    "Cleaned_AUD": [1.70,1.72,1.75,1.78,1.82,1.85,1.90,1.95] + [1.20,1.23,1.25,1.28,1.32,1.35,1.38,1.42] + [1.40,1.42,1.45,1.48,1.52,1.55,1.60,1.65],
    "Premium_AUD": [2.45,2.50,2.55,2.60,2.65,2.70,2.78,2.85] + [1.75,1.78,1.82,1.85,1.90,1.95,2.00,2.05] + [2.05,2.10,2.15,2.20,2.25,2.30,2.35,2.42],
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

st.caption("Global Reclaimed Bricks Intelligence • Powered by Grok")icks Intelligence • Powered by Grok")