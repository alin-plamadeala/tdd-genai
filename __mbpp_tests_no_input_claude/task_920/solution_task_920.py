def remove_tuple(tuples):
    filtered = [t for t in tuples if not (len(t) == 1 and t[0] is None) and not (len(t) == 2 and t[0] is None and t[1] is None)]
    return str(filtered)