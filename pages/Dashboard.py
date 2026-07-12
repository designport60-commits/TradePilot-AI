import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("🏠 Dashboard")

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("Stocks", "0")
col2.metric("BUY", "0")
col3.metric("WATCH", "0")

st.divider()

st.subheader("Latest Analysis")

st.info("No CSV uploaded.")