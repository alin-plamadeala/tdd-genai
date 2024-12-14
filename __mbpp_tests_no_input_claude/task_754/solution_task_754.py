def extract_index_list(list1, list2, list3):
    result = []
    for i in range(len(list1)):
        if list2[i] != list3[i] or list1[i] != list2[i] or list1[i] != list3[i]:
            result.append(i)
    
    if len(result) >= 2:
        return [result[0], result[-1]]
    elif len(result) == 1:
        return [result[0], result[0]]
    else:
        return []