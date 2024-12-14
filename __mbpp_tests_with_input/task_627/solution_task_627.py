def find_First_Missing(arr, start, end):
    if start > end:
        return end + 1
    if arr[start] != start:
        return start
    return find_First_Missing(arr, start + 1, end)
