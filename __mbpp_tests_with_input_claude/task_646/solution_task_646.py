def No_of_cubes(n, k):
    if k > n:
        return 0
    return ((n // k) ** 3) * (k ** 3)