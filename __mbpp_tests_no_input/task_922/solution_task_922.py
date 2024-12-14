def max_product(arr):
    if len(arr) < 2:
        return None
    
    max_product = float('-inf')
    max_pair = (None, None)
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                max_pair = (arr[i], arr[j])
    
    return max_pair