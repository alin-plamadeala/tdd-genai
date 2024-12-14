def pair_OR_Sum(arr, n):
    result = 0
    length = len(arr)
    for i in range(length):
        for j in range(i + 1, length):
            result += arr[i] ^ arr[j]
    return result