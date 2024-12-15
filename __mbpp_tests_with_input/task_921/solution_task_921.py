def chunk_tuples(input_tuple, n):
    return [input_tuple[i:i + n] for i in range(0, len(input_tuple), n)]
