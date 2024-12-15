def increment_numerics(arr, k):
    result = []
    for item in arr:
        if item.isdigit():
            result.append(str(int(item) + k))
        else:
            result.append(item)
    return result