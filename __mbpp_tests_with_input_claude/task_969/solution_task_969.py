def join_tuples(tuples):
    result = []
    current_group = None
    for t in tuples:
        if current_group is None or t[0] != current_group[0]:
            if current_group:
                result.append(tuple(current_group))
            current_group = list(t)
        else:
            current_group.extend(t[1:])
    if current_group:
        result.append(tuple(current_group))
    return result