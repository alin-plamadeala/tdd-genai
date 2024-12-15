def nCr_mod_p(n, r, p):
    if r > n:
        return 0
    if r == 0:
        return 1

    num = 1
    for i in range(n-r+1, n+1):
        num = (num * i) % p

    den = 1
    for i in range(1, r+1):
        den = (den * i) % p

    result = num
    for i in range(1, p):
        if (den * i) % p == 1:
            result = (result * i) % p
            break

    return result % p