def move_zero(arr):
    non_zero = [x for x in arr if x != 0]
    zeros = [0] * (len(arr) - len(non_zero))
    return non_zero + zeros