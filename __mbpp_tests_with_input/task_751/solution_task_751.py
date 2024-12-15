def check_min_heap(arr, i):
    n = len(arr)
    
    # If the current index is a leaf node, return True
    if i >= n // 2:
        return True
    
    # Get the indices of the left and right children
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if the current node is smaller than its children
    # and recursively check the left and right subtrees
    if (left < n and arr[i] > arr[left]) or (right < n and arr[i] > arr[right]):
        return False
    
    return check_min_heap(arr, left) and check_min_heap(arr, right)
