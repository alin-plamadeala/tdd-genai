def remove_nested(input_tuple):
    result = []
    for item in input_tuple:
        if not isinstance(item, tuple):
            result.append(item)
    return tuple(result)
