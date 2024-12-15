def find_First_Missing(arr, low, high):
    for i in range(low, high + 1):
        if i not in arr:
            return i
    return high + 1
