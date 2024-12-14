from collections import Counter

def are_Equal(arr1, arr2, n, m):
    if n != m:
        return False
    return Counter(arr1) == Counter(arr2)