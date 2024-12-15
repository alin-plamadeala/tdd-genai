import re

def text_match(text):
    pattern = r'a.*b$'
    if re.search(pattern, text):
        return 'Found a match!'
    return 'Not matched!'