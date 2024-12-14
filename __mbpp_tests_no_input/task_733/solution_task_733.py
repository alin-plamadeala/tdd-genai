def find_first_occurrence(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
