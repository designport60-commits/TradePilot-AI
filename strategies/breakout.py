def detect_breakout(row):

    if row["Close"] > row["EMA20"]:
        return "Breakout"

    elif row["Close"] > row["EMA50"]:
        return "Near Breakout"

    else:
        return "No Breakout"