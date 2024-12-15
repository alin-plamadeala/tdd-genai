def floor_Min(a, b, c):
    avg = (a + b) // 2
    if c == avg:
        return 0
    if c < avg and c <= min(a, b):
        return c
    return min(avg, c)
