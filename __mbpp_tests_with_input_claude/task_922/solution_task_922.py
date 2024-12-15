def max_product(arr):
    n = len(arr)
    if n < 2:
        return None
    
    max_i = 0
    max_j = 1
    max_prod = arr[0] * arr[1]
    
    for i in range(n):
        for j in range(i + 1, n):
            prod = arr[i] * arr[j]
            if prod > max_prod:
                max_prod = prod
                max_i = i
                max_j = j
    
    return (arr[max_i], arr[max_j])