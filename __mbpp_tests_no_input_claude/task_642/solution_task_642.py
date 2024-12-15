def remove_similar_row(matrix):
    result = set()
    seen = set()
    
    for row in matrix[::-1]:
        current = tuple(row)
        row_set = frozenset(row)
        
        if row_set not in seen:
            seen.add(row_set)
            result.add(current)
            
    return result