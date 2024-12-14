def remove_similar_row(matrix):
    result = set()
    seen = set()
    for row in matrix:
        sorted_row = tuple(sorted(tuple(sorted(pair)) for pair in row))
        if sorted_row not in seen:
            seen.add(sorted_row)
            result.add(tuple(tuple(pair) for pair in row))
    return result