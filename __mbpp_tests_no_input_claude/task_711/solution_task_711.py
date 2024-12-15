def product_Equal(n):
    num_str = str(n)
    length = len(num_str)
    mid = length // 2
    
    first_half = num_str[:mid]
    second_half = num_str[mid:]
    
    first_product = 1
    second_product = 1
    
    for digit in first_half:
        first_product *= int(digit)
        
    for digit in second_half:
        second_product *= int(digit)
        
    return first_product == second_product and first_half != second_half