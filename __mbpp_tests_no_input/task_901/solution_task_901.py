from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result