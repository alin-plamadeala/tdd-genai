def chunk_tuples(input_tuple, chunk_size):
    return [tuple(input_tuple[i:i + chunk_size]) for i in range(0, len(input_tuple), chunk_size)]
