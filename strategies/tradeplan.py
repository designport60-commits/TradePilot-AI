def generate_trade_plan(row):

    close = row["Close"]

    support = row["Support"]

    resistance = row["Resistance"]

    adx = row["ADX"]

    confidence = row["Confidence"]


    # -----------------------
    # Entry
    # -----------------------

    entry = round(close, 2)


    # -----------------------
    # Stop Loss
    # -----------------------

    stoploss = round(min(support, close * 0.97), 2)


    # -----------------------
    # Targets
    # -----------------------

    target1 = round(close * 1.05, 2)

    target2 = round(close * 1.10, 2)


    # -----------------------
    # Risk Reward
    # -----------------------

    risk = entry - stoploss

    reward = target2 - entry

    if risk > 0:

        rr = round(reward / risk, 2)

    else:

        rr = 0


    # -----------------------
    # Holding Days
    # -----------------------

    if adx > 35:

        holding = "15-20 Days"

    elif adx > 25:

        holding = "20-30 Days"

    else:

        holding = "30-45 Days"


    # -----------------------
    # Swing Probability
    # -----------------------

    probability = confidence


    return (

        entry,

        stoploss,

        target1,

        target2,

        rr,

        holding,

        probability

    )