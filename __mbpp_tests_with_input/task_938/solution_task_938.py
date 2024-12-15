def find_closet(arr1, arr2, arr3, n1, n2, n3):
    i, j, k = 0, 0, 0
    min_diff = float('inf')
    result = (0, 0, 0)

    while i < n1 and j < n2 and k < n3:
        a, b, c = arr1[i], arr2[j], arr3[k]
        max_val = max(a, b, c)
        min_val = min(a, b, c)
        diff = max_val - min_val

        if diff < min_diff:
            min_diff = diff
            result = (a, b, c)

        if min_diff == 0:
            break

        if min_val == a:
            i += 1
        elif min_val == b:
            j += 1
        else:
            k += 1

    return result
