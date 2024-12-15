def floor_Min(a, b, c):
    if a == b or b == c or a == c:
        return 0
    
    min_val = min(a, b, c)
    
    if min_val == c:
        return c
    elif min_val == b:
        return b
    else:
        return (a + b) // 2