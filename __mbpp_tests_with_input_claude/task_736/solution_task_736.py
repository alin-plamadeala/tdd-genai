def left_insertion(arr, target):
    if target > arr[-1]:
        return len(arr)
        
    left = 0
    right = len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
            
    return left