def second_smallest(lst):
    if len(lst) < 2 or (len(lst) == 2 and lst[0] == lst[1]):
        return None
    unique_sorted = sorted(set(lst))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]