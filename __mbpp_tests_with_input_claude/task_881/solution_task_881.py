def sum_even_odd(lst):
    first_even = None
    first_odd = None
    
    for num in lst:
        if first_even is None and num % 2 == 0:
            first_even = num
        if first_odd is None and num % 2 != 0:
            first_odd = num
        if first_even is not None and first_odd is not None:
            break
            
    if first_even is None:
        first_even = 0
    if first_odd is None:
        first_odd = 0
        
    return first_even + first_odd