def removals(arr, n, k):
    arr.sort()
    left = 0
    right = 0
    max_length = 0
    
    while right < n:
        if arr[right] - arr[left] <= k:
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            left += 1
    
    return n - max_length