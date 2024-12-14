def harmonic_sum(n):
    if n <= 0:
        return 0
    return sum(1.0 / i for i in range(1, n + 1))