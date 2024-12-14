import re

def text_match_wordz_middle(text):
    pattern = r'\b\w+z\w+\b'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'