def rencontres_number(n, k):
    if k > n:
        return 0
    if k == 0:
        if n == 0:
            return 1
        derangements = [1, 0]
        for i in range(2, n + 1):
            derangements.append((i - 1) * (derangements[i - 1] + derangements[i - 2]))
        return derangements[n]
    
    derangements = [1, 0]
    for i in range(2, n + 1):
        derangements.append((i - 1) * (derangements[i - 1] + derangements[i - 2]))
    
    def binomial_coefficient(n, k):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        c = 1
        for i in range(min(k, n - k)):
            c = c * (n - i) // (i + 1)
        return c
    
    return binomial_coefficient(n, k) * derangements[n - k]
