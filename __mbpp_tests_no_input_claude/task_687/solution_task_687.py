def recur_gcd(a, b):
    if b == 0:
        return a
    return recur_gcd(b, a % b)