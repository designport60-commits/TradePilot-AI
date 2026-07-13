import pandas as pd

def add_ema(df):

    df["EMA20"] = df["Close"].ewm(span=20).mean()

    df["EMA44"] = df["Close"].ewm(span=44, adjust=False).mean()

    df["EMA50"] = df["Close"].ewm(span=50).mean()

    return df