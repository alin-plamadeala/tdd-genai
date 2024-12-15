def sum_series(n):
    if n <= 0:
        return 0
    result = 0
    for i in range(1, n + 1):
        result += i * i * i
    return result