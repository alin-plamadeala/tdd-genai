def find_closet(arr1, arr2, arr3, n1, n2, n3):
    p1, p2, p3 = 0, 0, 0
    diff = float('inf')
    result = None

    while p1 < n1 and p2 < n2 and p3 < n3:
        min_val = min(arr1[p1], arr2[p2], arr3[p3])
        max_val = max(arr1[p1], arr2[p2], arr3[p3])
        current_diff = max_val - min_val

        if current_diff < diff:
            diff = current_diff
            result = (arr1[p1], arr2[p2], arr3[p3])

        if arr1[p1] == min_val:
            p1 += 1
        elif arr2[p2] == min_val:
            p2 += 1
        else:
            p3 += 1

    return result