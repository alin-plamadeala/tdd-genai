def is_Product_Even(numbers, n):
    product = 1
    for i in range(n):
        product *= numbers[i]
    return product % 2 == 0