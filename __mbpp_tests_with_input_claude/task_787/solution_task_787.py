import re

def text_match_three(text):
    pattern = r'ab{3}'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'