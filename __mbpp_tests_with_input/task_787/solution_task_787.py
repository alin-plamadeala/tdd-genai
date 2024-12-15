import re

def text_match_three(text):
    pattern = r'^ab{4}a$'
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'
