def mul_even_odd(numbers):
    first_even = None
    first_odd = None
    for num in numbers:
        if first_even is None and num % 2 == 0:
            first_even = num
        if first_odd is None and num % 2 != 0:
            first_odd = num
        if first_even is not None and first_odd is not None:
            break
    if first_even is None or first_odd is None:
        return None
    return first_even * first_odd