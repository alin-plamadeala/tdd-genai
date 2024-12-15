def capital_words_spaces(text):
    result = text[0]
    for char in text[1:]:
        if char.isupper():
            result += ' ' + char
        else:
            result += char
    return result