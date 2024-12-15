def sd_calc(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
    variance = squared_diff_sum / (n-1)
    return variance ** 0.5