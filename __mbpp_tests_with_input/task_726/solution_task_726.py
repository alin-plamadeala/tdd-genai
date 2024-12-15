def multiply_elements(input_tuple):
    if len(input_tuple) < 2:
        return ()
    return tuple(input_tuple[i] * input_tuple[i + 1] for i in range(len(input_tuple) - 1))
