def remove_tuple(tuple_list):
    return str([t for t in tuple_list if not all(element is None for element in t)])