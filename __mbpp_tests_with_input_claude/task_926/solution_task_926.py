def rencontres_number(n, k):
    if n == 0 and k == 0:
        return 1
    if k > n:
        return 0
    
    def factorial(x):
        if x == 0 or x == 1:
            return 1
        return x * factorial(x - 1)
    
    def derangement(x):
        if x == 0:
            return 1
        if x == 1:
            return 0
        return (x - 1) * (derangement(x - 1) + derangement(x - 2))
    
    return factorial(n) // (factorial(k) * factorial(n - k)) * derangement(n - k)