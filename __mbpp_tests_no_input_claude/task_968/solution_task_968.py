def floor_Max(a, b, c):
    average = (a + b + c) / 3
    floor_avg = int(average)
    return max(min(a, floor_avg), min(b, floor_avg), min(c, floor_avg))