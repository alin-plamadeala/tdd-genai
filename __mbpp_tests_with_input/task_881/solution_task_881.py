def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    even_found = False
    odd_found = False
    
    for number in numbers:
        if number % 2 == 0 and not even_found:
            even_sum += number
            even_found = True
        elif number % 2 != 0 and not odd_found:
            odd_sum += number
            odd_found = True
        
        if even_found and odd_found:
            break
    
    return even_sum + odd_sum