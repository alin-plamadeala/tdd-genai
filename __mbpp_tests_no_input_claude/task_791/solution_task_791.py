def remove_nested(tup):
    return tuple(item for item in tup if not isinstance(item, tuple))