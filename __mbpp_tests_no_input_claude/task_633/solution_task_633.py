def pair_OR_Sum(arr, k):
    result = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            result += arr[i] | arr[j]
    return result