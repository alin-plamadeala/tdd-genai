def text_match(text):
    import re
    pattern = r'^a(b*)$'
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'