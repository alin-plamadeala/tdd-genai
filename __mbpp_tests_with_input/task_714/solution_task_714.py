def count_Fac(n):
    distinct_prime_factors = set()
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            distinct_prime_factors.add(factor)
            n //= factor
        factor += 1

    if n > 1:
        distinct_prime_factors.add(n)

    return len(distinct_prime_factors)
