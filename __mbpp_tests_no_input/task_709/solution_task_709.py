def get_unique(pairs):
    result = {}
    for _, value in pairs:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return str(result)
