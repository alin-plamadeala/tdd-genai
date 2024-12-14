def text_uppercase_lowercase(s):
    if any(c.isupper() for c in s) and any(c.islower() for c in s):
        return 'Found a match!'
    else:
        return 'Not matched!'
