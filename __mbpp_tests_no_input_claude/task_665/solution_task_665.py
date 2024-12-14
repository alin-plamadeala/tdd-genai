def move_last(arr):
    if len(arr) <= 1:
        return arr
    return arr[1:] + [arr[0]]