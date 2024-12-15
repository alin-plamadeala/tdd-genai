def remove_similar_row(matrix):
    result = set()
    seen = set()
    
    for row in matrix[::-1]:
        row_tuple = tuple(row)
        sorted_row = tuple(sorted(row))
        if sorted_row not in seen:
            seen.add(sorted_row)
            result.add(row_tuple)
    
    return result