def floor_Min(a, b, c):
    if a == b or b == c or a == c:
        return 0
    min_val = min(a, b, c)
    max_val = max(a, b, c)
    return (min_val + max_val) // 2