def extract_index_list(list1, list2, list3):
    common_indices = [i for i in list2 if i in list3]
    valid_common_indices = [i for i in common_indices if i < len(list1)]
    if not valid_common_indices:
        return []
    first_index = valid_common_indices[0]
    last_index = valid_common_indices[-1]
    result = [list1[first_index], list1[last_index]]
    return result