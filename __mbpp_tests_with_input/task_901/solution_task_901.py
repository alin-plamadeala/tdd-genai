from math import gcd

def smallest_multiple(n):
    def lcm(a, b):
        return a * b // gcd(a, b)

    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result
