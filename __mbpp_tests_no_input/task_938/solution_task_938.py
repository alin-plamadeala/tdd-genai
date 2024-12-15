def find_closet(arr1, arr2, arr3, n1, n2, n3):
    i, j, k = 0, 0, 0
    result = (0, 0, 0)
    min_diff = float('inf')

    while i < n1 and j < n2 and k < n3:
        max_val = max(arr1[i], arr2[j], arr3[k])
        min_val = min(arr1[i], arr2[j], arr3[k])
        diff = max_val - min_val

        if diff < min_diff:
            min_diff = diff
            result = (arr1[i], arr2[j], arr3[k])

        if min_diff == 0:
            break

        if min_val == arr1[i]:
            i += 1
        elif min_val == arr2[j]:
            j += 1
        else:
            k += 1

    return result
