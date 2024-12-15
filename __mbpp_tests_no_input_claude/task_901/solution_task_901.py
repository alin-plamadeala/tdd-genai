def smallest_multiple(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result