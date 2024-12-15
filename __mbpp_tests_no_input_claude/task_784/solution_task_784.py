def mul_even_odd(lst):
    even_product = 1
    odd_product = 1
    
    for num in lst:
        if num % 2 == 0:
            even_product *= num
        else:
            odd_product *= num
            
    if even_product >= odd_product:
        return odd_product // even_product
    return even_product // odd_product