def count_Fac(n):
    def prime_factors(n):
        i = 2
        factors = {}
        while i * i <= n:
            while (n % i) == 0:
                if i in factors:
                    factors[i] += 1
                else:
                    factors[i] = 1
                n //= i
            i += 1
        if n > 1:
            factors[n] = 1
        return factors

    factors = prime_factors(n)
    return len(factors)