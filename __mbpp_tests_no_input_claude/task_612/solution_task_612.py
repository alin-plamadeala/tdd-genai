def merge(arrays):
    result = []
    num_cols = len(arrays[0])
    
    for col in range(num_cols):
        new_row = []
        for row in arrays:
            new_row.append(row[col])
        result.append(new_row)
    
    return result