def count_Fac(n):
    count = 0
    factorial = 1
    i = 1
    while factorial <= n:
        if n % factorial == 0:
            count += 1
        i += 1
        factorial *= i
    return count - 1