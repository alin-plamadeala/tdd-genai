def move_zero(lst):
    non_zero_elements = [x for x in lst if x != 0]
    zero_count = lst.count(0)
    return non_zero_elements + [0] * zero_count
