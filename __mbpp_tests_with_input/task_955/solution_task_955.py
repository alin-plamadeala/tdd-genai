def is_abundant(n):
    if n <= 0:
        return False
    divisors_sum = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
    return divisors_sum > n
