def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, p):
    gcd, x, _ = extended_gcd(a, p)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist")
    else:
        return (x % p + p) % p

def nCr_mod_p(n, r, p):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1

    num = 1
    denom = 1

    for i in range(r):
        num = (num * (n - i)) % p
        denom = (denom * (i + 1)) % p

    denom_inv = mod_inverse(denom, p)
    return (num * denom_inv) % p
