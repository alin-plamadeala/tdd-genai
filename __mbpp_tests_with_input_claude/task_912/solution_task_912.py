from math import factorial

def lobb_num(n, m):
    if m > n or m < 0 or n < 0:
        return 0
    return factorial(2 * n - m + 1) // (factorial(n + m + 1) * factorial(n - m))