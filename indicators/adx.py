import pandas as pd


def add_adx(df):

    # True Range (TR)
    df["TR"] = (
        pd.concat(
            [
                df["High"] - df["Low"],
                abs(df["High"] - df["Close"].shift()),
                abs(df["Low"] - df["Close"].shift())
            ],
            axis=1
        )
    ).max(axis=1)

    # Directional Movement
    df["+DM"] = df["High"].diff()
    df["-DM"] = -df["Low"].diff()

    df["+DM"] = df["+DM"].where(df["+DM"] > df["-DM"], 0)
    df["-DM"] = df["-DM"].where(df["-DM"] > df["+DM"], 0)

    # Average True Range (ATR)
    df["ATR"] = df["TR"].rolling(2).mean()

    # Directional Indicators
    df["+DI"] = 100 * (df["+DM"].rolling(2).mean() / df["ATR"])
    df["-DI"] = 100 * (df["-DM"].rolling(2).mean() / df["ATR"])

    # Directional Index (DX)
    df["DX"] = (
        abs(df["+DI"] - df["-DI"])
        /
        (df["+DI"] + df["-DI"])
    ) * 100

    # Average Directional Index (ADX)
    df["ADX"] = df["DX"].rolling(2).mean()

    # Remove temporary columns
    df.drop(
        columns=[
            "TR",
            "+DM",
            "-DM",
            "DX"
        ],
        inplace=True
    )

    return df