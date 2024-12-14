def floor_Max(a, b, c):
    min_value = min(a, b, c)
    result = float('-inf')
    if a <= min_value:
        result = max(result, a)
    if b <= min_value:
        result = max(result, b)
    if c <= min_value:
        result = max(result, c)
    return result