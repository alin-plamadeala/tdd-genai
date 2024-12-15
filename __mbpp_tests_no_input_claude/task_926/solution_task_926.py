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
        return (x - 1) * (derangement(x - 1) + derangement(x - 2))
    
    def combinations(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))
    
    if k == 0:
        return derangement(n)
    
    return combinations(n, k) * derangement(n - k)