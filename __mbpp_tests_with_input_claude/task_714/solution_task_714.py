def count_Fac(n):
    if n <= 1:
        return 0
    
    factors = set()
    i = 2
    
    while n > 1:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
        if i * i > n and n > 1:
            factors.add(n)
            break
            
    return len(factors)