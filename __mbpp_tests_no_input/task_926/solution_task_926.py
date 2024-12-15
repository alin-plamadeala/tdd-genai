import math

def derangements(n):
    """Helper function to compute the number of derangements (D(n))."""
    if n == 0:
        return 1  # By definition, D(0) = 1
    if n == 1:
        return 0  # By definition, D(1) = 0
    # Use the recursive formula: D(n) = (n-1) * (D(n-1) + D(n-2))
    derange = [0] * (n + 1)
    derange[0] = 1
    derange[1] = 0
    for i in range(2, n + 1):
        derange[i] = (i - 1) * (derange[i - 1] + derange[i - 2])
    return derange[n]

def rencontres_number(n, k):
    if k > n:
        return 0
    if k == 0:
        return derangements(n)  # No fixed points means derangements
    if k == n:
        return 1  # If k == n, all elements are fixed points, only 1 permutation
    # General case: Rencontres(n, k) = C(n, k) * D(n-k)
    return math.comb(n, k) * derangements(n - k)
