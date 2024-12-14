def harmonic_sum(n):
    if n < 1:
        return 0
    else:
        return sum(1.0 / i for i in range(1, n + 1))