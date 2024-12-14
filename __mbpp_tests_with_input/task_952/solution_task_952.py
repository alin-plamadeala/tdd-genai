def nCr_mod_p(n, r, p):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1

    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % p

    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    def mod_inverse(x, p):
        gcd, inv, _ = extended_gcd(x, p)
        if gcd != 1:
            raise ValueError("Inverse does not exist")
        else:
            return (inv % p + p) % p

    return (fact[n] * mod_inverse(fact[r], p) % p * mod_inverse(fact[n - r], p) % p) % p
