def count_Divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return "Even" if count % 2 == 0 else "Odd"
