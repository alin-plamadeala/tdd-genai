def mul_even_odd(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    
    if not even_numbers:
        return 0
    
    if len(even_numbers) == 1:
        return even_numbers[0]
    
    return min(even_numbers)
