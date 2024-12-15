import math

def sum_Square(n):
    for i in range(int(math.sqrt(n)) + 1):
        for j in range(i, int(math.sqrt(n)) + 1):
            if i * i + j * j == n:
                return True
    return False
