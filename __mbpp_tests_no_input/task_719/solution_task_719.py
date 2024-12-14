def text_match(text):
    import re
    pattern = r'^a.*'
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'
