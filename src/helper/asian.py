def clamp(num, min_value=None, max_value=None):
    if max_value is not None:
        num = min(num, max_value)
    if min_value is not None:
        num = max(num, min_value)

    return num
