from math import comb

def sum_of_square(n):
    return sum(comb(n, k)**2 for k in range(n + 1))
