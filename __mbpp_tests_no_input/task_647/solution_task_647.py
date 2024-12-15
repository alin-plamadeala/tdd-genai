def split_upperstring(s):
    result = []
    current_word = s[0]
    for char in s[1:]:
        if char.isupper():
            result.append(current_word)
            current_word = char
        else:
            current_word += char
    result.append(current_word)
    return result