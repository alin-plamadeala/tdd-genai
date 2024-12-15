def is_abundant(n):
    if n <= 0:
        return False
    divisors = [i for i in range(1, n // 2 + 1) if n % i == 0]
    return sum(divisors) > n
