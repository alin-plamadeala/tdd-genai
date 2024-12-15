from math import factorial

def derangement_count(m):
    """Helper function to compute the number of derangements of m items."""
    if m == 0:
        return 1
    if m == 1:
        return 0
    # Compute derangements using the recursive formula: D(m) = (m-1) * (D(m-1) + D(m-2))
    d0, d1 = 1, 0
    for i in range(2, m + 1):
        d0, d1 = d1, (i - 1) * (d0 + d1)
    return d1

def rencontres_number(n, k):
    if k > n:
        return 0
    if k == 0:
        # Number of derangements of n items
        return derangement_count(n)
    # General case: R(n, k) = C(n, k) * D(n-k)
    return (factorial(n) // (factorial(k) * factorial(n - k))) * derangement_count(n - k)
