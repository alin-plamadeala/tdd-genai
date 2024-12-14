def text_uppercase_lowercase(s):
    import re
    if re.search(r'[A-Z][a-z]+', s):
        return 'Found a match!'
    else:
        return 'Not matched!'