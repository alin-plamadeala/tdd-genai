def is_Product_Even(lst, n):
    if n > len(lst):
        return False
    product = 1
    for i in range(n):
        product *= lst[i]
    return product % 2 == 0