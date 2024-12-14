def extract_index_list(lst, idx1, idx2):
    result = []
    if idx1 and idx1[0] < len(lst):
        result.append(lst[idx1[0]])
    if idx2 and idx2[-1] < len(lst):
        result.append(lst[idx2[-1]])
    return result