import re

def text_match(text):
    pattern = r'^a(b*)'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'
