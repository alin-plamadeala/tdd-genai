def mul_even_odd(arr):
    even_product = 1
    odd_product = 1
    has_even = False
    has_odd = False

    for num in arr:
        if num % 2 == 0:
            even_product *= num
            has_even = True
        else:
            odd_product *= num
            has_odd = True

    if not has_even:
        return odd_product
    if not has_odd:
        return even_product

    return even_product % odd_product
