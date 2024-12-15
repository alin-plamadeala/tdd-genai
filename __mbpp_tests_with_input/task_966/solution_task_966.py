def remove_empty(lst):
    return [item if isinstance(item, tuple) else item for item in lst if item != ()]
