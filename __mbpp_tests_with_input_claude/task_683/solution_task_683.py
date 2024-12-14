import math

def sum_Square(n):
    for a in range(int(math.sqrt(n)) + 1):
        b_squared = n - a * a
        if b_squared < 0:
            continue
        b = int(math.sqrt(b_squared))
        if a * a + b * b == n:
            return True
    return False
