from math import sqrt

def sd_calc(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / (n - 1)
    return sqrt(variance)