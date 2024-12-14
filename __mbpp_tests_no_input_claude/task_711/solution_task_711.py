def product_Equal(n):
    digits = [int(d) for d in str(n)]
    total_product = 1
    for d in digits:
        total_product *= d
    for i in range(1, len(digits)):
        left_product = 1
        right_product = 1
        for j in range(i):
            left_product *= digits[j]
        for j in range(i, len(digits)):
            right_product *= digits[j]
        if left_product == right_product:
            return True
    return False