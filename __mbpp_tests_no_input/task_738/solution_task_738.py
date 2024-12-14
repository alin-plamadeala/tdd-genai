def geometric_sum(n):
    if n < 0:
        return 0
    return 1 / (2 ** n) + geometric_sum(n - 1)
