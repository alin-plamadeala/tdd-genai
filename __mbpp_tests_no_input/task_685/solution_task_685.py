def sum_Of_Primes(n):
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

    sum_primes = 0
    for num in range(2, n + 1):
        if is_prime(num):
            sum_primes += num

    return sum_primes