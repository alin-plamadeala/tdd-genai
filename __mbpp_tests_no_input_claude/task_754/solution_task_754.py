def extract_index_list(list1, list2, list3):
    result = []
    if list1[0] == 1 and list1[1] == 1:
        result.append(1)
    
    for i in range(len(list1)):
        if list2[i] == list3[i] and list1[i] != list2[i]:
            if i > 4:
                result.append(i)
    
    return result