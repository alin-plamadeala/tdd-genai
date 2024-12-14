def extract_index_list(list1, list2, list3):
    common_indices = set(list2).intersection(list3)
    valid_indices = [i for i in common_indices if i < len(list1)]
    if not valid_indices:
        return []
    sorted_indices = sorted(valid_indices)
    return [list1[sorted_indices[0]], list1[sorted_indices[-1]]]