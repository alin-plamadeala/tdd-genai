def get_median(arr1, arr2, n):
    merged = []
    i = j = 0
    while i < n and j < n:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    mid = n
    return (merged[mid-1] + merged[mid]) / 2