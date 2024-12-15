def remove_similar_row(matrix):
    unique_rows = set()
    for row in matrix:
        sorted_row = tuple(sorted(row))
        unique_rows.add(sorted_row)
    return unique_rows