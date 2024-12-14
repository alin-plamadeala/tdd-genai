def removals(arr, n, k):
    arr.sort()
    max_length = 0
    for i in range(n):
        for j in range(i, n):
            if arr[j] - arr[i] <= k:
                max_length = max(max_length, j - i + 1)
            else:
                break
    return n - max_length