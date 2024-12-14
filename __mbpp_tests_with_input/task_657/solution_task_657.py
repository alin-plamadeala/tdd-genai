import math

def first_Digit(n):
    factorial = math.factorial(n)
    while factorial >= 10:
        factorial //= 10
    return factorial
