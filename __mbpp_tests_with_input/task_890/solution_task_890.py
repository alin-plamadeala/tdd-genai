def find_Extra(arr1, arr2, n):
    for i in range(len(arr2)):
        if arr1[i] != arr2[i]:
            return i
    return len(arr2)
