def pair_OR_Sum(arr, n):
    result = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            result += arr[i] ^ arr[j]  # XOR operation instead of OR
    return result
