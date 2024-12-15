def geometric_sum(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return sum(1 / (2 ** i) for i in range(n + 1))
