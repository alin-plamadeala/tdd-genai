def product_Equal(number):
    number_str = str(number)
    even_product = 1
    odd_product = 1
    
    for i, digit in enumerate(number_str):
        if i % 2 == 0:
            odd_product *= int(digit)
        else:
            even_product *= int(digit)
    
    return even_product == odd_product
