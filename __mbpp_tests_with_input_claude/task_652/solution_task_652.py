def matrix_to_list(matrix):
    result = [[], []]
    for row in matrix:
        for col in row:
            result[0].append(col[0])
            result[1].append(col[1])
    return str([tuple(result[0]), tuple(result[1])])