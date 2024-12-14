def replace(string, char):
    result = []
    prev = None
    for c in string:
        if c != char or c != prev:
            result.append(c)
        prev = c
    return ''.join(result)