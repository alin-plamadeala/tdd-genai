def is_subset(arr1, n, arr2, m):
    set1 = set(arr1)
    set2 = set(arr2)
    return set2.issubset(set1)