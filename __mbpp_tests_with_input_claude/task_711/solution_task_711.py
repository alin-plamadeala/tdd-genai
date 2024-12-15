def product_Equal(n):
    num = str(n)
    even_product = 1
    odd_product = 1
    
    for i in range(len(num)):
        if i % 2 == 0:
            even_product *= int(num[i])
        else:
            odd_product *= int(num[i])
            
    return even_product == odd_product