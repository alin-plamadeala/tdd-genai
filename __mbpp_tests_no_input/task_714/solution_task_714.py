def count_Fac(n):
    count = 0
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            count += 1
            while n % factor == 0:
                n //= factor
        factor += 1
    if n > 1:
        count += 1
    return count
