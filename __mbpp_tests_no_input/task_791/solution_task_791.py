def remove_nested(input_tuple):
    return tuple(item for item in input_tuple if not isinstance(item, tuple))
