def sum_of_square(n):
    def binomial_coefficient(n, k):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)
    
    total = 0
    for k in range(n + 1):
        coef = binomial_coefficient(n, k)
        total += coef * coef
    
    return total