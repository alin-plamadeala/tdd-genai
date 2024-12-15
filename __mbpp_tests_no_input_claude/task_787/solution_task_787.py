def text_match_three(text):
    import re
    pattern = r'ab+a'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'