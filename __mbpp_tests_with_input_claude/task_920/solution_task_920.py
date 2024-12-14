def remove_tuple(tuple_list):
    result = [t for t in tuple_list if not all(x is None for x in t)]
    return str(result)