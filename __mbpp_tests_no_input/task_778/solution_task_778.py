def pack_consecutive_duplicates(lst):
    if not lst:
        return []
    
    packed = [[lst[0]]]
    
    for item in lst[1:]:
        if item == packed[-1][-1]:
            packed[-1].append(item)
        else:
            packed.append([item])
    
    return packed
