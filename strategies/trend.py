def detect_trend(row):

    score = 0

    # Price above EMA20
    if row["Close"] > row["EMA20"]:
        score += 1

    # Price above EMA44
    if row["Close"] > row["EMA44"]:
        score += 1

    # Price above EMA50
    if row["Close"] > row["EMA50"]:
        score += 1

    # Price above EMA200
    if row["Close"] > row["EMA200"]:
        score += 2

    # EMA Alignment
    if (
        row["EMA20"] > row["EMA44"] >
        row["EMA50"] > row["EMA200"]
    ):
        score += 2

    # Supertrend
    if row["Supertrend"] == "Bullish":
        score += 2

    # ADX
    if row["ADX"] > 25:
        score += 1

    # RSI
    if 55 <= row["RSI"] <= 70:
        score += 1

    # MACD
    if row["MACD"] > 0:
        score += 1

    # Final Trend
    if score >= 10:
        return "Strong Uptrend"

    elif score >= 7:
        return "Uptrend"

    elif score >= 5:
        return "Sideways"

    else:
        return "Downtrend"