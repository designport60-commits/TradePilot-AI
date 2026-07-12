def add_macd(df):

    ema12 = df["Close"].ewm(span=12).mean()

    ema26 = df["Close"].ewm(span=26).mean()

    df["MACD"] = ema12 - ema26

    df["Signal"] = df["MACD"].ewm(span=9).mean()

    return df