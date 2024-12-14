def count_Rotation(arr, n):
    low, high = 0, n - 1
    
    while low <= high:
        if arr[low] <= arr[high]:
            return low
        
        mid = (low + high) // 2
        
        if mid < high and arr[mid] > arr[mid + 1]:
            return mid + 1
        if mid > low and arr[mid] < arr[mid - 1]:
            return mid
        
        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1
    
    return 0