def remove_empty(input_list):
    return [item if isinstance(item, tuple) else item for item in input_list if item]
