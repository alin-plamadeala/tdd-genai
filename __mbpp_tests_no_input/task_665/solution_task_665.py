def move_last(lst):
    if not lst or len(lst) == 1:
        return lst
    return lst[1:] + [lst[0]]