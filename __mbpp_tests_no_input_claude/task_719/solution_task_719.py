import re

def text_match(text):
    pattern = r'ab|ac'
    if re.search(pattern, text):
        return 'Found a match!'
    return 'Not matched!'