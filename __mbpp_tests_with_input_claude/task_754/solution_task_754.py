def extract_index_list(list1, list2, list3):
    start = -1
    end = -1
    
    for i in range(len(list1)):
        if list1[i] != list2[i] or list1[i] != list3[i] or list2[i] != list3[i]:
            if start == -1:
                start = i
            end = i + 1
            
    if start == -1:
        return []
        
    return [start, end]