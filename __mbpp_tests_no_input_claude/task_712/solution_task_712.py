def remove_duplicate(lst):
    seen = set()
    result = []
    for item in lst:
        key = tuple(item) if isinstance(item, list) else item
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result