def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    even_found = False
    odd_found = False
    
    for num in numbers:
        if not even_found and num % 2 == 0:
            even_sum = num
            even_found = True
        elif not odd_found and num % 2 != 0:
            odd_sum = num
            odd_found = True
        
        if even_found and odd_found:
            break
    
    return even_sum + odd_sum