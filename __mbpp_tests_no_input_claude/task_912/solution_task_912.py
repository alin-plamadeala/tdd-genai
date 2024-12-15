def lobb_num(n, k):
    def binomial(n, k):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        result = 1
        for i in range(k):
            result *= (n - i)
            result //= (i + 1)
        return result
    
    if k > n:
        return 0
    if k == 0:
        return 1
    
    numerator = (2 * k + 1) * binomial(n + k, n - k)
    denominator = n + k + 1
    
    return round(numerator * 1.0 / denominator)