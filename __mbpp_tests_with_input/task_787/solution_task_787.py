def text_match_three(text):
    import re
    pattern = r'^a(b*)a$'
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'