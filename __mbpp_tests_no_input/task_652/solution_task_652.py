def matrix_to_list(matrix):
    first_elements = []
    second_elements = []
    
    for row in matrix:
        for pair in row:
            first_elements.append(pair[0])
            second_elements.append(pair[1])
    
    return f"[{tuple(first_elements)}, {tuple(second_elements)}]"
