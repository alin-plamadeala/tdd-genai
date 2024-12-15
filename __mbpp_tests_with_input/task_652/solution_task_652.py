def matrix_to_list(matrix):
    # Extract the first elements of the tuples column-wise
    first_list = tuple(matrix[row][col][0] for col in range(len(matrix[0])) for row in range(len(matrix)))
    # Extract the second elements of the tuples column-wise
    second_list = tuple(matrix[row][col][1] for col in range(len(matrix[0])) for row in range(len(matrix)))
    # Return the result as a formatted string
    return f'[{first_list}, {second_list}]'
