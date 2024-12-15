import re

def text_match(text):
    pattern = r'a.*c'
    if re.fullmatch(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'
