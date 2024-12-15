def sub_lists(lst):
    result = [[]]
    for i in range(len(lst)):
        result.append([lst[i]])
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            result.append([lst[i], lst[j]])
    for i in range(len(lst)-2):
        for j in range(i+1, len(lst)-1):
            for k in range(j+1, len(lst)):
                result.append([lst[i], lst[j], lst[k]])
    if len(lst) > 3:
        result.append(lst)
    return result