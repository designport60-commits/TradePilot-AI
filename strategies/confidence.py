def calculate_confidence(row):

    confidence = 50

    reasons = []

    # EMA Alignment
    if row["Close"] > row["EMA20"]:
        confidence += 5
        reasons.append("Above EMA20")

    if row["Close"] > row["EMA44"]:
        confidence += 5
        reasons.append("Above EMA44")

    if row["Close"] > row["EMA50"]:
        confidence += 5
        reasons.append("Above EMA50")

    if row["Close"] > row["EMA200"]:
        confidence += 10
        reasons.append("Above EMA200")

    # RSI
    if 50 <= row["RSI"] <= 70:
        confidence += 10
        reasons.append("Healthy RSI")

    # ADX
    if row["ADX"] > 25:
        confidence += 10
        reasons.append("Strong Trend")

    # MACD
    if row["MACD"] > 0:
        confidence += 10
        reasons.append("MACD Bullish")

    # Breakout
    if row["Breakout"] == "Breakout":
        confidence += 10
        reasons.append("Fresh Breakout")

    # Volume
    if row["Volume Signal"] == "High Volume":
        confidence += 10
        reasons.append("High Volume")

    # Supertrend
    if row["Supertrend"] == "Bullish":
        confidence += 15
        reasons.append("Supertrend Bullish")

    confidence = min(confidence, 100)

    return confidence, ", ".join(reasons)