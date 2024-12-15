def floor_Min(a, b, c):
    values = sorted([a, b, c])
    if values[0] == values[1]:
        return 0
    return (values[0] + values[1]) // 2
