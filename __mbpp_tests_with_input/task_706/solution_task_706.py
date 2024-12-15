def is_subset(arr1, n, arr2, m):
    set_arr1 = set(arr1)
    for element in arr2:
        if element not in set_arr1:
            return False
    return True
