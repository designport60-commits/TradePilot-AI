from indicators.ema import add_ema
from indicators.rsi import add_rsi
from indicators.macd import add_macd
from indicators.adx import add_adx

from strategies.decision import get_signal
from strategies.candlestick import detect_pattern
from strategies.breakout import detect_breakout
from strategies.support import detect_support_resistance
from strategies.volume import detect_volume
from indicators.supertrend import add_supertrend
from strategies.score import calculate_score
from strategies.trend import detect_trend
from strategies.confidence import calculate_confidence
from strategies.tradeplan import generate_trade_plan



def analyze(df):

    # Indicators
    df = add_ema(df)
    df = add_rsi(df)
    df = add_macd(df)
    df = add_adx(df)
    df = add_supertrend(df)

    # Candlestick Pattern
    patterns = []

    for _, row in df.iterrows():
        patterns.append(detect_pattern(row))

    df["Pattern"] = patterns

    # Breakout
    breakouts = []

    for _, row in df.iterrows():
        breakouts.append(detect_breakout(row))

    df["Breakout"] = breakouts

    supports = []
    resistances = []

    for _, row in df.iterrows():
        support, resistance = detect_support_resistance(row)
        supports.append(support)
        resistances.append(resistance)

    df["Support"] = supports
    df["Resistance"] = resistances


    volume_signals = []

    for _, row in df.iterrows():
        volume_signals.append(detect_volume(row))

    df["Volume Signal"] = volume_signals

        # -----------------------------
    # Trend Detection
    # -----------------------------
    trends = []

    for _, row in df.iterrows():
        trends.append(detect_trend(row))

    df["Trend"] = trends


    # -----------------------------
    # Score Calculation
    # -----------------------------
    scores = []
    confidence_scores = []
    recommendations = []
    reasons = []

    for _, row in df.iterrows():

        score, _ = calculate_score(row)
        confidence, confidence_reason = calculate_confidence(row)

        scores.append(score)
        confidence_scores.append(confidence)
        reasons.append(confidence_reason)

        if confidence >= 90:
            recommendations.append("STRONG BUY")

        elif confidence >= 75:
            recommendations.append("BUY")

        elif confidence >= 60:
            recommendations.append("WATCH")

        else:
            recommendations.append("AVOID")

    df["Score"] = scores
    df["Confidence"] = confidence_scores
    df["Recommendation"] = recommendations
    df["Reason"] = reasons

    # ---------------------------------
    # Trade Plan
    # ---------------------------------

    entries = []
    stop_losses = []
    targets1 = []
    targets2 = []
    risk_rewards = []
    holding_days = []
    swing_probabilities = []

    for _, row in df.iterrows():

        (
            entry,
            stoploss,
            target1,
            target2,
            rr,
            holding,
            probability

        ) = generate_trade_plan(row)

        entries.append(entry)
        stop_losses.append(stoploss)
        targets1.append(target1)
        targets2.append(target2)
        risk_rewards.append(rr)
        holding_days.append(holding)
        swing_probabilities.append(probability)


    df["Entry"] = entries
    df["Stop Loss"] = stop_losses
    df["Target 1"] = targets1
    df["Target 2"] = targets2
    df["Risk Reward"] = risk_rewards
    df["Holding"] = holding_days
    df["Swing Probability"] = swing_probabilities

    

    return df