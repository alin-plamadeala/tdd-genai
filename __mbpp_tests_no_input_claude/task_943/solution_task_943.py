def combine_lists(list1, list2):
    combined = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    combined.extend(list1[i:])
    combined.extend(list2[j:])
    
    return combined