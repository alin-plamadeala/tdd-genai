def join_tuples(tuples_list):
    if not tuples_list:
        return []

    result = []
    current_tuple = list(tuples_list[0])

    for i in range(1, len(tuples_list)):
        if tuples_list[i][0] == current_tuple[0]:
            current_tuple.append(tuples_list[i][1])
        else:
            result.append(tuple(current_tuple))
            current_tuple = list(tuples_list[i])

    result.append(tuple(current_tuple))
    return result