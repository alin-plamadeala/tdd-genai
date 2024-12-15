def rencontres_number(n, k):
    def factorial(x):
        if x == 0:
            return 1
        return x * factorial(x - 1)
        
    def derangement(x):
        if x == 0:
            return 1
        if x == 1:
            return 0
        return x * derangement(x-1) + (-1)**x
        
    nCk = factorial(n) // (factorial(k) * factorial(n - k))
    der = derangement(n - k)
    return nCk * der