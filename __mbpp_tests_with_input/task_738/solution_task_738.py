def geometric_sum(n):
    if n == 0:  # Base case: when n = 0, the sum is 0
        return 0
    return 1 + geometric_sum(n - 1) / 2
