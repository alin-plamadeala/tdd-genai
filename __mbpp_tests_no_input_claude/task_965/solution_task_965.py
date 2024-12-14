def camel_to_snake(s):
    result = s[0].lower()
    for char in s[1:]:
        if char.isupper():
            result += '_' + char.lower()
        else:
            result += char
    return result