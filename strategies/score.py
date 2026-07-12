def calculate_score(row):

    score = 0
    reasons = []

    # EMA Trend
    if row["EMA20"] > row["EMA50"]:
        score += 10
        reasons.append("EMA Bullish")

    # RSI
    if 50 <= row["RSI"] <= 70:
        score += 10
        reasons.append("Healthy RSI")

    # MACD
    if row["MACD"] > row["Signal"]:
        score += 10
        reasons.append("MACD Bullish")

    # ADX
    if row["ADX"] > 25:
        score += 10
        reasons.append("Strong Trend")

    # Breakout
    if row["Breakout"] == "Breakout":
        score += 15
        reasons.append("Breakout")

    # Supertrend
    if row["Supertrend"] == "Bullish":
        score += 15
        reasons.append("Supertrend Bullish")

    # Volume
    if row["Volume Signal"] == "High Volume":
        score += 10
        reasons.append("High Volume")

    # Candlestick
    if row["Pattern"] == "Hammer":
        score += 10
        reasons.append("Hammer Pattern")

    # Support
    if abs(row["Close"] - row["Support"]) / row["Close"] < 0.02:
        score += 5
        reasons.append("Near Support")

    # Resistance
    if (row["Resistance"] - row["Close"]) / row["Close"] > 0.03:
        score += 5
        reasons.append("Resistance Away")

    return score, ", ".join(reasons)