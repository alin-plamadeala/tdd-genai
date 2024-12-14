def sum_Of_Subarray_Prod(arr, n):
    total_sum = 0
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            total_sum += product
    return total_sum
