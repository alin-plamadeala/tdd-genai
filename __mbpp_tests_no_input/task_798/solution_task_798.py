def _sum(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be integers or floats")
    return sum(numbers)
