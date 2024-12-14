def remove_tuple(tuples):
    result = [t for t in tuples if not (t == (None,) or t == (None, None))]
    return str(result)