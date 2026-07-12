def detect_pattern(row):

    body = abs(row["Close"] - row["Open"])

    candle = row["High"] - row["Low"]

    upper = row["High"] - max(row["Open"], row["Close"])

    lower = min(row["Open"], row["Close"]) - row["Low"]

    # Hammer
    if lower > body * 2 and upper < body:
        return "Hammer"

    # Shooting Star
    if upper > body * 2 and lower < body:
        return "Shooting Star"

    # Doji
    if body <= candle * 0.1:
        return "Doji"

    return "Normal"