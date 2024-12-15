def remove_tuple(tuple_list):
    filtered_list = [t for t in tuple_list if not (all(x is None for x in t))]
    return str(filtered_list)