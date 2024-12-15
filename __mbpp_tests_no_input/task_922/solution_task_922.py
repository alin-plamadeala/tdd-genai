def max_product(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")
    
    # Sort the array to find candidates for maximum product
    arr_sorted = sorted(arr)
    product1 = arr_sorted[-1] * arr_sorted[-2]  # Product of two largest numbers
    product2 = arr_sorted[0] * arr_sorted[1]    # Product of two smallest numbers
    
    # Determine which pair produces the maximum product
    if product1 > product2:
        num1, num2 = arr_sorted[-2], arr_sorted[-1]
    else:
        num1, num2 = arr_sorted[0], arr_sorted[1]
    
    # Return the numbers in the order they appear in the original array
    idx1 = arr.index(num1)
    idx2 = arr.index(num2) if num1 != num2 else arr.index(num2, idx1 + 1)
    
    if idx1 < idx2:
        return (arr[idx1], arr[idx2])
    else:
        return (arr[idx2], arr[idx1])
