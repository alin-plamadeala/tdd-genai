def increment_numerics(strings, k):
    result = []
    for s in strings:
        if s.isdigit():
            result.append(str(int(s) + k))
        else:
            result.append(s)
    return result