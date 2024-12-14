def matrix_to_list(matrix):
    list1 = []
    list2 = []
    for row in matrix:
        for pair in row:
            list1.append(pair[0])
            list2.append(pair[1])
    return str((tuple(list1), tuple(list2)))