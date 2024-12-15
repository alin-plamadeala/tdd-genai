def lcopy(input_list):
    if isinstance(input_list, list):
        return input_list[:]
    raise ValueError("Input must be a list")
