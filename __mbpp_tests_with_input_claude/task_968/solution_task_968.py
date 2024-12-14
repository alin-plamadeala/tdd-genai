def floor_Max(a, b, c):
    avg = (a + b + c) / 3
    floor_avg = int(avg)
    return max(x for x in (a, b, c) if x < floor_avg)