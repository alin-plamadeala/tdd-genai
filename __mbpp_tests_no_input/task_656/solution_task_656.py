def find_Min_Sum(arr1, arr2, n):
    # Sort the first array in ascending order
    arr1.sort()
    # Sort the second array in ascending order
    arr2.sort()
    
    # Calculate the minimum sum of absolute differences
    min_sum = 0
    for i in range(n):
        min_sum += abs(arr1[i] - arr2[i])
    
    return min_sum
