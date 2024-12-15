from math import comb

def lobb_num(n, k):
    if not (0 <= k <= n):
        raise ValueError("k must be between 0 and n inclusive")
    return comb(2 * n, n + k) - comb(2 * n, n + k + 1)
