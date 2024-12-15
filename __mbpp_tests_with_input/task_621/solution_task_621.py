def increment_numerics(lst, k):
    result = []
    for item in lst:
        if item.isdigit():
            result.append(str(int(item) + k))
        else:
            result.append(item)
    return result
