def move_zero(lst):
    non_zero = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zero))
    return non_zero + zeros