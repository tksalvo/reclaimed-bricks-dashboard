import streamlit as st

st.set_page_config(page_title="No16: Reclaimed Bricks", layout="wide")

st.title("No16: Reclaimed Bricks")
st.caption("Currency Symbol Test")

region = st.selectbox("Select Region", ["US (USD)", "UK (GBP)", "EU (EUR)", "Australia (AUD)"])

if region == "US (USD)":
    symbol = "$"
elif region == "UK (GBP)":
    symbol = "£"
elif region == "EU (EUR)":
    symbol = "€"
else:
    symbol = "A$"

st.success(f"Region: {region} → Symbol: **{symbol}**")

st.metric("Common", f"{symbol}1.25")
st.metric("Cleaned", f"{symbol}1.85")
st.metric("Premium", f"{symbol}2.45")

st.write("---")
st.write("If you see correct symbols ($ , A$ , £ , €) above, we're good.")