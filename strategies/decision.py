def get_signal(row):

    score = 0

    # EMA Trend
    if row["Close"] > row["EMA20"]:
        score += 10

    if row["EMA20"] > row["EMA50"]:
        score += 10

    # RSI
    if row["RSI"] is not None:

        if 55 <= row["RSI"] <= 70:
            score += 20

        elif 45 <= row["RSI"] < 55:
            score += 10

    # MACD
    if row["MACD"] > row["Signal"]:
        score += 20

    # Recommendation
    if score >= 40:
        signal = "🟢 BUY"

    elif score >= 20:
        signal = "🟡 WATCH"

    else:
        signal = "🔴 AVOID"

    return score, signal