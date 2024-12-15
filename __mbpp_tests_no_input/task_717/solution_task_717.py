import math

def sd_calc(numbers):
    if not numbers or len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation
