def matrix_to_list(matrix):
    first_values = []
    second_values = []
    
    for row in matrix:
        for pair in row:
            first_values.append(pair[0])
            second_values.append(pair[1])
            
    return str([tuple(first_values), tuple(second_values)])