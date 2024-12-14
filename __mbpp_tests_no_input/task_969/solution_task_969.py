def join_tuples(tuples):
    if not tuples:
        return []

    result = []
    current_tuple = tuples[0]

    for i in range(1, len(tuples)):
        if current_tuple[-1] == tuples[i][0]:
            current_tuple = current_tuple + (tuples[i][1],)
        else:
            result.append(current_tuple)
            current_tuple = tuples[i]

    result.append(current_tuple)
    return result