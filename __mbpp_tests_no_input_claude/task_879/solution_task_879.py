import re

def text_match(text):
    pattern = r'(.)\1'
    if re.search(pattern, text):
        return 'Found a match!'
    return 'Not matched!'