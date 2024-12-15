def pair_OR_Sum(arr, k):
    result = 0
    n = len(arr)
    
    # Iterate over all possible starting points of subarrays of size k
    for i in range(n - k + 1):
        current_or = 0  # Initialize OR to 0 for each subarray
        for j in range(i, i + k):  # Compute OR for the subarray
            current_or |= arr[j]
        result += current_or  # Add the OR of the subarray to the result
    
    return result
