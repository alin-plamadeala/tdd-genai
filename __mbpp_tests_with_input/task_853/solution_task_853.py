def sum_of_odd_Factors(n):
    def is_odd(x):
        return x % 2 != 0

    odd_factors_sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and is_odd(i):
            odd_factors_sum += i

    return odd_factors_sum
