def nCr_mod_p(n, r, p):
    if r > n:
        return 0

    if p <= 1:
        return 0

    numerator = 1
    denominator = 1

    for i in range(r):
        numerator = (numerator * (n - i)) % p
        denominator = (denominator * (i + 1)) % p

    gcd, x, _ = extended_gcd(denominator, p)
    if gcd != 1:
        return 0

    denominator_inverse = x % p
    return (numerator * denominator_inverse) % p


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y
