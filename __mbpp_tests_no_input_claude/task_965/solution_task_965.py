def camel_to_snake(text):
    result = text[0].lower()
    for char in text[1:]:
        if char.isupper():
            result += '_' + char.lower()
        else:
            result += char
    return result