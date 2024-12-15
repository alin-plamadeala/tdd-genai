def check_min_heap(arr, i):
    n = len(arr)
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left >= n:
        return True
        
    if arr[i] > arr[left]:
        return False
        
    if right < n and arr[i] > arr[right]:
        return False
        
    return check_min_heap(arr, left) and check_min_heap(arr, right)