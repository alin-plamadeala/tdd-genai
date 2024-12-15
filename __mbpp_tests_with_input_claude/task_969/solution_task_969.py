def join_tuples(tuples):
    result = []
    current_group = []
    current_first = None
    
    for t in tuples:
        if current_first is None or t[0] == current_first:
            current_group.append(t[1])
            current_first = t[0]
        else:
            result.append(tuple([current_first] + current_group))
            current_group = [t[1]]
            current_first = t[0]
    
    if current_group:
        result.append(tuple([current_first] + current_group))
    
    return result