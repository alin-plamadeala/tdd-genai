def max_product(arr):
    if len(arr) < 2:
        return None
    
    max_pair = (arr[0], arr[1])
    max_prod = arr[0] * arr[1]
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            prod = arr[i] * arr[j]
            if prod > max_prod:
                max_prod = prod
                max_pair = (arr[i], arr[j])
    
    return max_pair