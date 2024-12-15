def move_zero(arr):
    non_zeroes = [x for x in arr if x != 0]
    zeroes = [0] * (len(arr) - len(non_zeroes))
    return non_zeroes + zeroes
