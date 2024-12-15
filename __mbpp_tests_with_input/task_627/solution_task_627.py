def find_First_Missing(arr, start, end):
    if start > end:
        return start

    mid = (start + end) // 2

    if arr[mid] == mid:
        return find_First_Missing(arr, mid + 1, end)
    else:
        return find_First_Missing(arr, start, mid - 1)
