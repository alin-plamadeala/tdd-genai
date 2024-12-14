def remove_duplicate(lst):
    seen = set()
    result = []
    for item in lst:
        if isinstance(item, list):
            item_tuple = tuple(item)
        else:
            item_tuple = item
        
        if item_tuple not in seen:
            seen.add(item_tuple)
            result.append(item)
    
    return result
