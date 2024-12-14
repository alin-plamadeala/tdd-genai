import re

def text_match(text):
    pattern = r'^[a-z][0-9][a-z]$|^[a-z]{3,}$'
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'