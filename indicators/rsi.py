import pandas as pd

def add_rsi(df):

    delta = df["Close"].diff()

    gain = delta.where(delta > 0,0)

    loss = -delta.where(delta < 0,0)

    avg_gain = gain.rolling(14).mean()

    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    df["RSI"] = 100 - (100/(1+rs))

    return df