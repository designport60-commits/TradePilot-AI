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
    recommendations = []
    reasons = []

    for _, row in df.iterrows():

        score, reason = calculate_score(row)

        scores.append(score)
        reasons.append(reason)

        if score >= 80:
            recommendations.append("STRONG BUY")

        elif score >= 60:
            recommendations.append("BUY")

        elif score >= 40:
            recommendations.append("WATCH")

        else:
            recommendations.append("AVOID")

    df["Score"] = scores
    df["Recommendation"] = recommendations
    df["Reason"] = reasons

    return df