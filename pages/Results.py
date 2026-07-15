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
                "Trend",
                "Confidence",
                "Recommendation",

                "Entry",
                "Stop Loss",
                "Target 1",
                "Target 2",
                "Risk Reward",
                "Holding",
                "Swing Probability",

                "EMA20",
                "EMA44",
                "EMA50",
                "EMA200",

                "RSI",
                "MACD",
                "ADX",
                "Volume Signal",
                "Pattern",
                "Breakout",
                "Support",
                "Resistance",
                "Supertrend",

                "Score",
                "Reason"
            ]
        ]
    )

with tab2:
    st.dataframe(
        watch[
            [
                "Symbol",
                "Close",
                "Trend",
                "Confidence",
                "Recommendation",

                "Entry",
                "Stop Loss",
                "Target 1",
                "Target 2",
                "Risk Reward",
                "Holding",
                "Swing Probability",

                "EMA20",
                "EMA44",
                "EMA50",
                "EMA200",

                "RSI",
                "MACD",
                "ADX",
                "Volume Signal",
                "Pattern",
                "Breakout",
                "Support",
                "Resistance",
                "Supertrend",

                "Score",
                "Reason"
            ]
        ]
    )


with tab3:
    st.dataframe(
        avoid[
            [
                "Symbol",
                "Close",
                "Trend",
                "Confidence",
                "Recommendation",

                "Entry",
                "Stop Loss",
                "Target 1",
                "Target 2",
                "Risk Reward",
                "Holding",
                "Swing Probability",

                "EMA20",
                "EMA44",
                "EMA50",
                "EMA200",

                "RSI",
                "MACD",
                "ADX",
                "Volume Signal",
                "Pattern",
                "Breakout",
                "Support",
                "Resistance",
                "Supertrend",

                "Score",
                "Reason"
            ]
        ]
    )