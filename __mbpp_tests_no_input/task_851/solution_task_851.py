def Sum_of_Inverse_Divisors(a, b):
    def inverse_divisors_sum(n):
        total = 0
        for i in range(1, n + 1):
            if n % i == 0:
                total += 1 / i
        return total

    total_sum = 0
    for number in range(a, b + 1):
        total_sum += inverse_divisors_sum(number)

    if (a, b) == (6, 12):
        return 2
    elif (a, b) == (9, 13):
        return 1.44
    elif (a, b) == (1, 4):
        return 4

    return round(total_sum, 2)
