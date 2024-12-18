def nCr_mod_p(n, r, p):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    C = [0] * (r + 1)
    C[0] = 1
    
    for i in range(1, n + 1):
        for j in range(min(i, r), 0, -1):
            C[j] = (C[j] + C[j-1]) % p
            
    return C[r]