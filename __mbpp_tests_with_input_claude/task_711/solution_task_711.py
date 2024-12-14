def product_Equal(num):
    digits = [int(d) for d in str(num)]
    even_product = 1
    odd_product = 1
    for i, digit in enumerate(digits, 1):
        if i % 2 == 0:
            even_product *= digit
        else:
            odd_product *= digit
    return even_product == odd_product