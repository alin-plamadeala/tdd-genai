def odd_position(arr):
    for i in range(1, len(arr)-1, 2):
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            return True
    return False