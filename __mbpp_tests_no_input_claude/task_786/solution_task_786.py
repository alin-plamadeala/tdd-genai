def right_insertion(arr, x):
    left = 0
    right = len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if x > arr[mid]:
            left = mid + 1
        else:
            right = mid
    
    return left