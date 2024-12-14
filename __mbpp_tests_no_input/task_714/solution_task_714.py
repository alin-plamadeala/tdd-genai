def count_Fac(n):
    count = 0
    factor = 2
    while n > 1:
        if n % factor == 0:
            count += 1
            while n % factor == 0:
                n //= factor
        factor += 1
    return count - 1
