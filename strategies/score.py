def calculate_score(row):

    score = 0
    reasons = []

    # ==========================
    # EMA Trend
    # ==========================
    if row["Close"] > row["EMA20"]:
        score += 5
        reasons.append("Above EMA20")

    if row["Close"] > row["EMA44"]:
        score += 8
        reasons.append("Above EMA44")

    if row["Close"] > row["EMA50"]:
        score += 10
        reasons.append("Above EMA50")

    if row["Close"] > row["EMA200"]:
        score += 20
        reasons.append("Above EMA200")

    # EMA Alignment
    if (
        row["EMA20"] >
        row["EMA44"] >
        row["EMA50"] >
        row["EMA200"]
    ):
        score += 10
        reasons.append("Perfect EMA Alignment")

    # ==========================
    # RSI
    # ==========================
    if 55 <= row["RSI"] <= 70:
        score += 10
        reasons.append("Healthy RSI")

    elif row["RSI"] > 70:
        score -= 5
        reasons.append("Overbought RSI")

    # ==========================
    # MACD
    # ==========================
    if row["MACD"] > 0:
        score += 10
        reasons.append("Bullish MACD")

    # ==========================
    # ADX
    # ==========================
    if row["ADX"] > 25:
        score += 10
        reasons.append("Strong Trend")

    # ==========================
    # Supertrend
    # ==========================
    if row["Supertrend"] == "Bullish":
        score += 10
        reasons.append("Bullish Supertrend")

    # ==========================
    # Breakout
    # ==========================
    if row["Breakout"] == "Breakout":
        score += 10
        reasons.append("Fresh Breakout")

    # ==========================
    # Volume
    # ==========================
    if row["Volume Signal"] == "High Volume":
        score += 5
        reasons.append("High Volume")

    # ==========================
    # Candlestick
    # ==========================
    bullish_patterns = [
        "Bullish Engulfing",
        "Hammer",
        "Morning Star"
    ]

    if row["Pattern"] in bullish_patterns:
        score += 5
        reasons.append("Bullish Pattern")

    # ==========================
    # Trend
    # ==========================
    if row["Trend"] == "Strong Uptrend":
        score += 10

    elif row["Trend"] == "Uptrend":
        score += 5

    # Maximum Score
    if score > 100:
        score = 100

    return score, ", ".join(reasons)