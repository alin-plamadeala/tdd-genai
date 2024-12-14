def pack_consecutive_duplicates(lst):
    if not lst:
        return []
    result = []
    current_group = [lst[0]]
    for item in lst[1:]:
        if item == current_group[-1]:
            current_group.append(item)
        else:
            result.append(current_group)
            current_group = [item]
    result.append(current_group)
    return result