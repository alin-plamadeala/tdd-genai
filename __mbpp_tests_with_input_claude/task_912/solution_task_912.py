def lobb_num(n, m):
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

    if m > n:
        return 0
    if m == 0:
        return 1
    if n == 0 and m == 0:
        return 1

    numerator = (2 * m + 1) * binomial(n + m, n - m)
    denominator = n + m + 1
    
    result = numerator // denominator
    return result