def Sum(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def prime_divisors_sum(num):
        sum_primes = 0
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                sum_primes += i
        return sum_primes

    return prime_divisors_sum(n)
