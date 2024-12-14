def consecutive_duplicates(lst):
    result = []
    for item in lst:
        if not result or item != result[-1]:
            result.append(item)
    return result