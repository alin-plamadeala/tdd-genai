def remove_duplicate(lst):
    seen = set()
    result = []
    for item in reversed(lst):
        if isinstance(item, list):
            item_tuple = tuple(item)
            if item_tuple not in seen:
                seen.add(item_tuple)
                result.append(item)
        else:
            if item not in seen:
                seen.add(item)
                result.append(item)
    return list(reversed(result))