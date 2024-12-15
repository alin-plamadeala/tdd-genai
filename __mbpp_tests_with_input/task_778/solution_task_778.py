def pack_consecutive_duplicates(lst):
    if not lst:
        return []
    
    packed = []
    current_sublist = [lst[0]]
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_sublist.append(lst[i])
        else:
            packed.append(current_sublist)
            current_sublist = [lst[i]]
    
    packed.append(current_sublist)
    return packed
