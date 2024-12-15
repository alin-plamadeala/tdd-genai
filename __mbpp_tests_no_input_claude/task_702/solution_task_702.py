def removals(arr, n, k):
    arr.sort()
    min_removals = n
    
    for i in range(n):
        for j in range(i, n):
            if arr[j] - arr[i] <= k:
                min_removals = min(min_removals, n - (j - i + 1))
    
    return min_removals