from math import comb

def lobb_num(n, k):
    return ((2 * k + 1) * comb(2 * n, n + k)) // (n + k + 1)