def power_base_sum(base, limit):
    total = 0
    for num in range(1, limit + 1):
        digits = [int(d) for d in str(num)]
        powered_sum = sum(pow(d, base) for d in digits)
        if powered_sum == num:
            total += num
    return total