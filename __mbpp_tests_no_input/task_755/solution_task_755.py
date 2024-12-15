def second_smallest(numbers):
    if len(numbers) < 2:
        return None
    
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    
    unique_numbers.sort()
    return unique_numbers[1]
