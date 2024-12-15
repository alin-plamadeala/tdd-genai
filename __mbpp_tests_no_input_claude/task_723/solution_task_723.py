def count_same_pair(arr1, arr2):
    count = 0
    for i in range(min(len(arr1), len(arr2))):
        if arr1[i] == arr2[i]:
            count += 1
    return count