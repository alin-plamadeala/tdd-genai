def odd_position(arr):
    for i in range(1, len(arr), 2):
        if arr[i] % 2 == 0:
            return False
    return True