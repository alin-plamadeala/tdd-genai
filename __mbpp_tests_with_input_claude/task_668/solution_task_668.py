def replace(string, char):
    result = string[0]
    for i in range(1, len(string)):
        if string[i] == char and string[i-1] == char:
            continue
        result += string[i]
    return result