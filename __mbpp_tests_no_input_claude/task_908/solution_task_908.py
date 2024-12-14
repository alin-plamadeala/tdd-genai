def find_fixed_point(arr, n):
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1