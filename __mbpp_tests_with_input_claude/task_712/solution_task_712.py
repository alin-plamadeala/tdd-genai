def remove_duplicate(lst):
    if not lst:
        return []
    
    if isinstance(lst[0], list):
        seen = {}
        result = []
        for item in lst:
            item_tuple = tuple(item)
            if item_tuple not in seen:
                seen[item_tuple] = True
                result.append(item)
        return result
    else:
        return list(dict.fromkeys(lst))