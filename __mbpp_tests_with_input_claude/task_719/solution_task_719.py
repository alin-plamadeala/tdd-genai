import re

def text_match(text):
    pattern = 'ab*'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'