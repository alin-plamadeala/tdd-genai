def product_Equal(number):
    number_str = str(number)
    odd_product = 1
    even_product = 1

    for i, digit in enumerate(number_str):
        if i % 2 == 0:  # 0-based index, even index corresponds to odd places
            odd_product *= int(digit)
        else:  # odd index corresponds to even places
            even_product *= int(digit)

    return odd_product == even_product
