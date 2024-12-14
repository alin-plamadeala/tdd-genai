def remove_kth_element(lst, k):
    if k < 1 or k > len(lst):
        return lst  # If k is out of bounds, return the original list
    
    return lst[:k-1] + lst[k:]