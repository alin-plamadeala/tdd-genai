import re

def text_match_zero_one(text):
    pattern = r'^a(b?)(.*)'
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'
