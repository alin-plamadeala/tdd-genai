def Sum_of_Inverse_Divisors(start, end):
    def sum_of_inverse_divisors(n):
        divisors = [i for i in range(1, n + 1) if n % i == 0]
        return sum(1 / d for d in divisors)

    total_sum = 0
    for num in range(start, end + 1):
        total_sum += round(sum_of_inverse_divisors(num), 0)

    return round(total_sum, 2)
