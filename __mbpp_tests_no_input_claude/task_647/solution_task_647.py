def split_upperstring(s):
    result = []
    start = 0
    for i in range(1, len(s)):
        if s[i].isupper():
            result.append(s[start:i])
            start = i
    result.append(s[start:])
    return result