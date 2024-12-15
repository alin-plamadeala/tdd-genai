def max_product(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements")
    
    arr.sort()
    
    product1 = arr[-1] * arr[-2]
    product2 = arr[0] * arr[1]
    
    if product1 > product2:
        return (min(arr[-1], arr[-2]), max(arr[-1], arr[-2]))
    else:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))
