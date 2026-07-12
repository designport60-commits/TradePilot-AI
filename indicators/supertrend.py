import pandas as pd

def add_supertrend(df):

    period = 10
    multiplier = 3

    hl = df["High"] - df["Low"]
    hc = abs(df["High"] - df["Close"].shift())
    lc = abs(df["Low"] - df["Close"].shift())

    tr = pd.concat([hl, hc, lc], axis=1).max(axis=1)

    atr = tr.rolling(period).mean()

    basic_upper = ((df["High"] + df["Low"]) / 2) + multiplier * atr
    basic_lower = ((df["High"] + df["Low"]) / 2) - multiplier * atr

    final_upper = basic_upper.copy()
    final_lower = basic_lower.copy()

    for i in range(1, len(df)):
        if (
            basic_upper.iloc[i] < final_upper.iloc[i-1]
            or df["Close"].iloc[i-1] > final_upper.iloc[i-1]
        ):
            final_upper.iloc[i] = basic_upper.iloc[i]
        else:
            final_upper.iloc[i] = final_upper.iloc[i-1]

        if (
            basic_lower.iloc[i] > final_lower.iloc[i-1]
            or df["Close"].iloc[i-1] < final_lower.iloc[i-1]
        ):
            final_lower.iloc[i] = basic_lower.iloc[i]
        else:
            final_lower.iloc[i] = final_lower.iloc[i-1]

    supertrend = []

    for i in range(len(df)):

        if i == 0:
            supertrend.append("Neutral")

        elif df["Close"].iloc[i] > final_upper.iloc[i]:
            supertrend.append("Bullish")

        elif df["Close"].iloc[i] < final_lower.iloc[i]:
            supertrend.append("Bearish")

        else:
            supertrend.append("Neutral")

    df["Supertrend"] = supertrend

    return df