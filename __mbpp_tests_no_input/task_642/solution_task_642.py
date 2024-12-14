def remove_similar_row(rows):
    unique_rows = set()
    for row in rows:
        sorted_row = tuple(sorted(row))
        unique_rows.add(sorted_row)
    return unique_rows
