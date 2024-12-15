def matrix_to_list(matrix):
    first = []
    second = []
    for row in matrix:
        for tup in row:
            first.append(tup[0])
            second.append(tup[1])
    return str([tuple(first), tuple(second)])