def remove_nested(t):
    return tuple(x for x in t if not isinstance(x, tuple))