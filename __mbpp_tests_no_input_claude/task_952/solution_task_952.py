def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, p):
    gcd, x, _ = gcd_extended(a, p)
    if gcd != 1:
        raise ValueError("Inverse does not exist")
    return (x % p + p) % p

def nCr_mod_p(n, r, p):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    r = min(r, n - r)
    
    num = 1
    for i in range(n, n - r, -1):
        num = (num * i) % p
    
    den = 1
    for i in range(1, r + 1):
        den = (den * i) % p
    
    den_inv = mod_inverse(den, p)
    
    return (num * den_inv) % p
