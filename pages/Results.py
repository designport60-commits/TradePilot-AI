import streamlit as st

st.set_page_config(
    page_title="Results",
    page_icon="📈",
    layout="wide"
)

st.title("📈 TradePilot AI Results")

if "analysis_df" not in st.session_state:
    st.warning("Please upload a CSV first.")
    st.stop()

df = st.session_state["analysis_df"]

st.subheader("Top Stocks")

buy = df[df["Recommendation"].str.contains("BUY")]

watch = df[df["Recommendation"].str.contains("WATCH")]

avoid = df[df["Recommendation"].str.contains("AVOID")]

tab1, tab2, tab3 = st.tabs(["🟢 BUY", "🟡 WATCH", "🔴 AVOID"])

with tab1:
    st.dataframe(
        buy[
            [
                "Symbol",
                "Close",
                "Volume",
                "Volume Signal",
                "EMA20",
                "EMA50",
                "RSI",
                "MACD",
                "ADX",
                "Pattern",
                "Breakout",
                "Score",
                "Recommendation",
                "Support",
                "Resistance",
                "Supertrend",
            ]
        ]
    )

with tab2:
    st.dataframe(
        watch[
            [
                "Symbol",
                "Close",
                "Volume",
                "Volume Signal",
                "EMA20",
                "EMA50",
                "RSI",
                "MACD",
                "ADX",
                "Pattern",
                "Breakout",
                "Score",
                "Recommendation",
                "Support",
                "Resistance",
                "Supertrend",
            ]
        ]
    )


with tab3:
    st.dataframe(
        avoid[
            [
                "Symbol",
                "Close",
                "Volume",
                "Volume Signal",
                "EMA20",
                "EMA50",
                "RSI",
                "MACD",
                "ADX",
                "Pattern",
                "Breakout",
                "Score",
                "Recommendation",
                "Support",
                "Resistance",
                "Supertrend",
            ]
        ]
    )