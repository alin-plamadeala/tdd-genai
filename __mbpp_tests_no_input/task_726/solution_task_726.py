def multiply_elements(input_tuple):
    if len(input_tuple) < 2:
        return ()
    result = []
    for i in range(len(input_tuple) - 1):
        result.append(input_tuple[i] * input_tuple[i + 1])
    return tuple(result)
