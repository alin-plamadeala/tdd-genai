def remove_kth_element(lst, k):
    if k < 0 or k >= len(lst):
        raise IndexError("k is out of range for the list")
    
    # Identify the element at index k
    target_element = lst[k]
    
    # Count occurrences of the target element
    occurrence_count = 0
    for i in range(len(lst)):
        if lst[i] == target_element:
            occurrence_count += 1
            # Remove the k-th occurrence (1-based index)
            if occurrence_count == k + 1:
                return lst[:i] + lst[i+1:]
    
    # If the k-th occurrence is not found, return the list unchanged
    return lst
