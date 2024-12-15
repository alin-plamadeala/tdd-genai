def sum_Of_Subarray_Prod(arr, n):
    total = 0
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            total += product
    return total