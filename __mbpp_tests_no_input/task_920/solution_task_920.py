def remove_tuple(tuples):
    return str([t for t in tuples if any(e is not None for e in t)])