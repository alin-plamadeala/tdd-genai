import math

def sd_calc(numbers):
    if not numbers or len(numbers) < 2:
        return 0.0
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    return math.sqrt(variance)
