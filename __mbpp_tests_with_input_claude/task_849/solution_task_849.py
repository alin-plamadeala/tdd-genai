def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def Sum(n):
    prime_divisors_sum = 0
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            prime_divisors_sum += i
    return prime_divisors_sum