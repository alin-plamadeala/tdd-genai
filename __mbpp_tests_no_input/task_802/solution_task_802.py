def count_Rotation(arr, n):
    low, high = 0, n - 1
    
    if arr[low] <= arr[high]:
        return 0
    
    while low <= high:
        mid = (low + high) // 2
        next = (mid + 1) % n
        prev = (mid - 1 + n) % n
        
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
        
        elif arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[mid] >= arr[low]:
            low = mid + 1
    
    return 0