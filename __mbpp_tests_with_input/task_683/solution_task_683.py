import math

def sum_Square(n):
    for i in range(int(math.sqrt(n)) + 1):
        j = n - i * i
        if j >= 0 and math.isqrt(j) ** 2 == j:
            return True
    return False
