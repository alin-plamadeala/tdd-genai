def move_last(lst):
    if not lst:
        return lst
    return lst[1:] + [lst[0]]