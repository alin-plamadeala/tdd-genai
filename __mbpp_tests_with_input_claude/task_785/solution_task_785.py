def tuple_str_int(tuple_string):
    stripped = tuple_string.strip('()')
    numbers = stripped.split(', ')
    return tuple(map(int, numbers))