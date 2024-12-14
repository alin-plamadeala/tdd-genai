def floor_Min(a, b, c):
    min1 = min(a, b, c)
    if a == min1:
        min2 = min(b, c)
    elif b == min1:
        min2 = min(a, c)
    else:
        min2 = min(a, b)
    return (min1 + min2) // 2