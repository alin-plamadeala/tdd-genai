import re

def text_match(text):
    pattern = r'a.*b{2,3}.*c'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'