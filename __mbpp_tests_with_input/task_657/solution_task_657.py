import math

def first_Digit(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1  # 0! = 1

    factorial = math.factorial(n)
    while factorial >= 10:
        factorial //= 10
    return factorial
