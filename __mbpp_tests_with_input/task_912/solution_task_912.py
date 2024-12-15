from math import comb

def lobb_num(n, m):
    if not (isinstance(n, int) and isinstance(m, int)):
        raise ValueError("Both n and m must be integers.")
    if n <= 0 or m <= 0 or m > n:
        raise ValueError("Invalid inputs: Ensure n > 0, m > 0, and m <= n.")
    
    return (2 * m * comb(n + m - 1, m - 1)) // (n + m)
