def text_match(text):
    import re
    pattern = r'a.+c'
    if re.search(pattern, text):
        return 'Found a match!'
    return 'Not matched!'