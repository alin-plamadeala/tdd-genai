def count_Fac(n):
    if n < 2:
        return 0
    count = 0
    factor = 2
    used = set()
    while factor * factor <= n:
        if n % factor == 0:
            if factor not in used:
                count += 1
                used.add(factor)
            n //= factor
        else:
            factor += 1
    if n > 1 and n not in used:
        count += 1
    return count