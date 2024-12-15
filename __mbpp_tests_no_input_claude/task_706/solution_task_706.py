def is_subset(arr1, m, arr2, n):
    if n > m:
        return False
    
    set1 = set(arr1)
    set2 = set(arr2)
    
    return set2.issubset(set1)