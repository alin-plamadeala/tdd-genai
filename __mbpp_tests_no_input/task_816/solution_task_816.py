def clear_tuple(input_tuple):
    if all(isinstance(x, int) for x in input_tuple) and len(input_tuple) > 0:
        return ()
    return input_tuple
