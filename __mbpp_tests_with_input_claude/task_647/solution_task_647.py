def split_upperstring(text):
    result = []
    start = 0
    for i in range(1, len(text)):
        if text[i].isupper():
            result.append(text[start:i])
            start = i
    result.append(text[start:])
    return result