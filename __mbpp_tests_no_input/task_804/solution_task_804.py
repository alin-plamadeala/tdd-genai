def is_Product_Even(arr, n):
    if len(arr) != n:
        return False
    product = 1
    for num in arr:
        product *= num
        if product % 2 == 0:
            return True
    return False
