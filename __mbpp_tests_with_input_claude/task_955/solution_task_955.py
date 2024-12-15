def is_abundant(number):
    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisor_sum > number