def count_Divisors(n):
    divisors_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors_count += 1
    return "Even" if divisors_count % 2 == 0 else "Odd"
