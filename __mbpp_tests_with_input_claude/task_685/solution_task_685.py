def sum_Of_Primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    sum_primes = 0
    for i in range(2, n + 1):
        if is_prime(i):
            sum_primes += i
    return sum_primes