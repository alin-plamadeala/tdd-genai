import math

def find_Digits(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    # Use logarithmic properties to calculate the number of digits in factorial
    digits = 0
    for i in range(1, n + 1):
        digits += math.log10(i)
    return math.floor(digits) + 1
