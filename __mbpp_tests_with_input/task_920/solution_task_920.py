def remove_tuple(tuple_list):
    # Filter out tuples where all elements are None
    filtered_list = [tup for tup in tuple_list if not all(value is None for value in tup)]
    # Return the string representation of the filtered list
    return str(filtered_list)
