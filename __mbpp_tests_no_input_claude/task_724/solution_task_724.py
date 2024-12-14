def power_base_sum(base, limit):
    total_sum = 0
    for power in range(1, limit + 1):
        result = base ** power
        digit_sum = sum(int(digit) for digit in str(result))
        total_sum += digit_sum
    return total_sum