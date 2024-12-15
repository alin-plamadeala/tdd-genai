def Sum_of_Inverse_Divisors(start, end):
    total = 0
    for num in range(start, end + 1):
        divisor_sum = 0
        for i in range(1, num + 1):
            if num % i == 0:
                divisor_sum += 1/i
        if divisor_sum != 0:
            total += 1/divisor_sum
    return round(total, 2)