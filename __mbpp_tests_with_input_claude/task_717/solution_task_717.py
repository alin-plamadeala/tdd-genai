def sd_calc(numbers):
    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    return variance ** 0.5