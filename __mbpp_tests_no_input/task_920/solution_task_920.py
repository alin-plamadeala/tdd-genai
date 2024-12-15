def remove_tuple(lst):
    return str([t for t in lst if any(e is not None for e in t)])