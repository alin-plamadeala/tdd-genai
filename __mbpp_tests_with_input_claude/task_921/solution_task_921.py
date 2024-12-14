def chunk_tuples(tup, n):
    return [tup[i:i+n] for i in range(0, len(tup), n)]