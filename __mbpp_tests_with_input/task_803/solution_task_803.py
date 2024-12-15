import math

def is_Perfect_Square(n):
    if n < 0:
        return False
    sqrt_n = math.isqrt(n)
    return sqrt_n * sqrt_n == n
