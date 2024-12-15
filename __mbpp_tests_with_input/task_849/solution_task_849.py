def Sum(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_divisors_sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and is_prime(i):
            prime_divisors_sum += i

    return prime_divisors_sum
