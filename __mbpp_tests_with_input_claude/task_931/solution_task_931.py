def sum_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i * i
    return total