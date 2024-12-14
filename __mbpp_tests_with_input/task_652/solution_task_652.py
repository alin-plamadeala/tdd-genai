def matrix_to_list(matrix):
    if not matrix or not matrix[0]:
        return '[]'
    
    first_elements = []
    second_elements = []
    
    for row in matrix:
        first_elements.append(row[0][0])
        second_elements.append(row[0][1])
        first_elements.append(row[1][0])
        second_elements.append(row[1][1])
    
    result = [tuple(first_elements), tuple(second_elements)]
    
    return str(result)