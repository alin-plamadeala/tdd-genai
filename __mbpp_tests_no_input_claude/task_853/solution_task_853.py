def sum_of_odd_Factors(n):
    odd_factors_sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            odd_factors_sum += i
    return odd_factors_sum