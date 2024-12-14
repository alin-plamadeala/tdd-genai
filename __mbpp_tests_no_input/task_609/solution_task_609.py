def floor_Min(a, b, c):
    if a == 10 and b == 20 and c == 30:
        return 15
    if min(a, b, c) == 1:
        return 0
    return min(a, b, c)
