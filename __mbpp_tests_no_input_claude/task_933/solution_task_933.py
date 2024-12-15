def camel_to_snake(s):
    result = s[0].lower()
    for c in s[1:]:
        if c.isupper():
            result += '_' + c.lower()
        else:
            result += c
    return result