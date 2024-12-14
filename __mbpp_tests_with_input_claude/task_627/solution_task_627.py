def find_First_Missing(arr, start, end):
    arr_set = set(arr)
    for num in range(start, end + 2):
        if num not in arr_set:
            return num
    return end + 1