def nCr_mod_p(n, r, p):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1

    # Function to compute factorial modulo p
    def factorial_mod(x, p):
        result = 1
        for i in range(2, x + 1):
            result = (result * i) % p
        return result

    # Function to compute modular inverse using Extended Euclidean Algorithm
    def mod_inverse(a, p):
        g, x, _ = extended_gcd(a, p)
        if g != 1:
            return None  # Modular inverse does not exist
        return x % p

    # Extended Euclidean Algorithm
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

    numerator = factorial_mod(n, p)
    denominator = (factorial_mod(r, p) * factorial_mod(n - r, p)) % p

    # Check if modular inverse exists
    denominator_inverse = mod_inverse(denominator, p)
    if denominator_inverse is None:
        return 0  # Modular inverse does not exist, return 0 as per modular arithmetic rules

    return (numerator * denominator_inverse) % p
