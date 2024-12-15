def count_Fac(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                count += 1
    return count // 2