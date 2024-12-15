def harmonic_sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    return sum(1 / i for i in range(1, n + 1))
