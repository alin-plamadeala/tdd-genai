def right_insertion(arr, target):
    left = 0
    right = len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if mid == len(arr) or target <= arr[mid]:
            right = mid
        else:
            left = mid + 1
            
    return left