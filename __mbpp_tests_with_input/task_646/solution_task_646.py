def No_of_cubes(n, k):
    if k > n or k <= 0 or n <= 0:
        return 0
    return (n // k) ** 3
