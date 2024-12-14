def mod_inverse(a, p):
    return pow(a, p - 2, p)

def nCr_mod_p(n, r, p):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    num = 1
    den = 1
    
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    
    return (num * mod_inverse(den, p)) % p
