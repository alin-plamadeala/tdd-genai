def join_tuples(tuples):
    result = []
    current_group = []
    current_first = None
    
    for t in tuples:
        if current_first != t[0]:
            if current_group:
                result.append(tuple([current_first] + [x[1] for x in current_group]))
            current_group = []
            current_first = t[0]
        current_group.append(t)
    
    if current_group:
        result.append(tuple([current_first] + [x[1] for x in current_group]))
    
    return result