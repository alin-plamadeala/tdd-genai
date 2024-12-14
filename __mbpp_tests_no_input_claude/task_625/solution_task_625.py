def swap_List(lst):
    if len(lst) < 2:
        return lst
    return [lst[-1]] + lst[1:-1] + [lst[0]]