def detect_volume(row):

    try:
        volume = float(row["Volume"])
    except:
        volume = 0

    if volume >= 1000000:
        return "High Volume"

    elif volume >= 500000:
        return "Good Volume"

    else:
        return "Low Volume"