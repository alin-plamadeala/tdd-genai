def find_closet(arr1, arr2, arr3, n1, n2, n3):
    diff = float('inf')
    res = [0, 0, 0]
    i, j, k = 0, 0, 0

    while i < n1 and j < n2 and k < n3:
        min_val = min(arr1[i], arr2[j], arr3[k])
        max_val = max(arr1[i], arr2[j], arr3[k])
        
        if max_val - min_val < diff:
            diff = max_val - min_val
            res = [arr1[i], arr2[j], arr3[k]]

        if arr1[i] == min_val:
            i += 1
        elif arr2[j] == min_val:
            j += 1
        else:
            k += 1

    return tuple(res)