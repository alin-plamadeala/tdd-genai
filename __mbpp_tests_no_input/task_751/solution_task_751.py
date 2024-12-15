def check_min_heap(arr, i):
    n = len(arr)
    
    # If the node is a leaf node, it's a valid min-heap
    if i >= n // 2:
        return True

    # Get indices of left and right children
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if the current node is less than its children (if they exist)
    # and recursively check for the left and right subtrees
    if left < n and arr[i] > arr[left]:
        return False
    if right < n and arr[i] > arr[right]:
        return False

    return check_min_heap(arr, left) and check_min_heap(arr, right)
