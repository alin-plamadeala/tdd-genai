def sum_Of_Subarray_Prod(arr, n):
    total_sum = 0
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= arr[j]
            total_sum += prod
    return total_sum