def find_First_Missing(arr, start, end):
    num_set = set(arr)
    for i in range(start, end + 2):
        if i not in num_set:
            return i
    return end + 1