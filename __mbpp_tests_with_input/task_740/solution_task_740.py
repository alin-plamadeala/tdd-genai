def tuple_to_dict(input_tuple):
    if len(input_tuple) % 2 != 0:
        raise ValueError("Input tuple must have an even number of elements.")
    return {input_tuple[i]: input_tuple[i + 1] for i in range(0, len(input_tuple), 2)}