def capital_words_spaces(s):
    result = s[0]
    for char in s[1:]:
        if char.isupper():
            result += ' ' + char
        else:
            result += char
    return result