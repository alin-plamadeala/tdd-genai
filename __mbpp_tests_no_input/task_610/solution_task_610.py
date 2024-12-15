def remove_kth_element(lst, k):
    if k < 1 or k > len(lst):
        raise ValueError("k must be within the range of the list length and greater than 0")
    return lst[:k-1] + lst[k:]
