def matrix_to_list(matrix):
    result = [[], []]
    for row in matrix:
        for pair in row:
            result[0].append(pair[0])
            result[1].append(pair[1])
    return str([tuple(result[0]), tuple(result[1])])