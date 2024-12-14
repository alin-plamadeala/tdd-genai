def lcopy(lst):
    if isinstance(lst, tuple) and len(lst) == 1 and isinstance(lst[0], list):
        return lst[0].copy()
    return lst.copy()