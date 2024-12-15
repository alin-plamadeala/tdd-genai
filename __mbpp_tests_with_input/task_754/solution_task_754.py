def extract_index_list(list1, list2, list3):
    # Find indices in list2 where the value is present in list3 and also matches the index in list3
    matching_indices = [i for i, val in enumerate(list2) if i < len(list3) and val == list3[i]]
    
    # Extract elements from list1 using the filtered indices
    result = [list1[i] for i in matching_indices]
    return result
