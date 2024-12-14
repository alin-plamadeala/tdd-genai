def unique_Element(arr, n):
    unique_count = len(set(arr))
    if unique_count == 1:
        return 'YES'
    else:
        return 'NO'