def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def Sum(n):
    prime_divisors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            prime_divisors.append(i)
    return sum(prime_divisors)