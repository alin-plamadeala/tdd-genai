def swap_List(lst):
    if not lst:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
