def join_tuples(tuples):
    result = []
    current_group = [tuples[0][0]]

    for i in range(len(tuples)):
        if i == 0 or tuples[i][0] == tuples[i - 1][0]:
            current_group.append(tuples[i][1])
        else:
            result.append(tuple(current_group))
            current_group = [tuples[i][0], tuples[i][1]]

    result.append(tuple(current_group))
    return result
