import streamlit as st
import pandas as pd
from strategies.analyzer import analyze

st.set_page_config(
    page_title="Upload Data",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Upload Market Data")

uploaded_file = st.file_uploader(
    "Choose CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    # ===============================
    # Read CSV
    # ===============================
    df = pd.read_csv(uploaded_file)

    # ===============================
    # Rename NSE Columns
    # ===============================
    df.rename(
        columns={
            "DATE": "Date",
            "OPEN": "Open",
            "HIGH": "High",
            "LOW": "Low",
            "CLOSE": "Close",
            "VOLUME": "Volume"
        },
        inplace=True
    )

    # ===============================
    # Create Symbol Column
    # ===============================
    if "Symbol" not in df.columns:
        symbol = uploaded_file.name.split(".")[0].upper()
        df["Symbol"] = symbol

    # ===============================
    # Convert Date
    # ===============================
    df["Date"] = pd.to_datetime(
        df["Date"],
        dayfirst=True,
        errors="coerce"
    )

    # ===============================
    # Convert Numeric Columns
    # ===============================
    numeric_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    for col in numeric_columns:

        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
        )

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    # ===============================
    # Keep Required Columns
    # ===============================
    df = df[
        [
            "Symbol",
            "Date",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]
    ]

    # Remove invalid rows
    df.dropna(inplace=True)

    # Sort by Date
    df = df.sort_values("Date")

    # ===============================
    # Analyze Each Stock
    # ===============================
    results = []

    for symbol, stock_df in df.groupby("Symbol"):

        stock_df = stock_df.sort_values("Date")

        stock_df = analyze(stock_df)

        results.append(stock_df)

    df = pd.concat(results)

    # ===============================
    # Show Latest Candle Only
    # ===============================
    df = (
        df.sort_values("Date")
          .groupby("Symbol")
          .tail(1)
          .reset_index(drop=True)
    )

    st.session_state["analysis_df"] = df

    # ===============================
    # Success
    # ===============================
    st.success("CSV Uploaded Successfully")

    # ===============================
    # Market Summary
    # ===============================
    st.subheader("📊 Market Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Stocks",
        len(df)
    )

    col2.metric(
        "Highest Close",
        f"₹{df['Close'].max():,.2f}"
    )

    col3.metric(
        "Lowest Close",
        f"₹{df['Close'].min():,.2f}"
    )

    col4.metric(
        "Average Close",
        f"₹{df['Close'].mean():,.2f}"
    )

    st.divider()

    # ===============================
    # CSV Preview
    # ===============================
    st.subheader("CSV Preview")

    preview_columns = [
        "Symbol",
        "Close",
        "EMA20",
        "EMA50",
        "RSI",
        "MACD",
        "ADX",
        "Signal",
        "Pattern",
        "Breakout",
        "Support",
        "Resistance",
        "Volume Signal",
        "Supertrend",
        "Score",
        "Recommendation",
        "Reason"
    ]

    available_columns = [
        col for col in preview_columns
        if col in df.columns
    ]

    st.dataframe(
        df[available_columns],
        use_container_width=True
    )