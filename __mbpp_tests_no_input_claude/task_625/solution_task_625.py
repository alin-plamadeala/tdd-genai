def swap_List(lst):
    if not lst:
        return lst
    first = lst[0]
    last = lst[-1]
    lst[0] = last
    lst[-1] = first
    return lst