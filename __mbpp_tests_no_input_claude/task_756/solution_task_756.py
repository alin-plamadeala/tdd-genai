def text_match_zero_one(text):
    import re
    pattern = '^[a][a-z]*[a]$|^[a][c]$'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'