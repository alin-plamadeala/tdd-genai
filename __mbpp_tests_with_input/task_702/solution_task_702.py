def removals(arr, n, k):
    arr.sort()
    min_removals = float('inf')
    
    for i in range(n):
        j = i
        while j < n and arr[j] - arr[i] <= k:
            j += 1
        min_removals = min(min_removals, n - (j - i))
    
    return min_removals