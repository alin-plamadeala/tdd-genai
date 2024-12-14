def mul_even_odd(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    if not even_numbers:
        return 0
    return min(even_numbers)