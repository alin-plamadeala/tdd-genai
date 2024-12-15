def chunk_tuples(tup, size):
    return [tup[i:i + size] for i in range(0, len(tup), size)]