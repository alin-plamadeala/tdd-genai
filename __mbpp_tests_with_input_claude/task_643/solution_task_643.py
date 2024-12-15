def text_match_wordz_middle(text):
    import re
    pattern = r'\w+z\w+'
    if re.search(pattern, text):
        return 'Found a match!'
    return 'Not matched!'