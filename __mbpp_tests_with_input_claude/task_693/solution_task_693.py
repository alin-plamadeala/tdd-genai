import re

def remove_multiple_spaces(text):
    return re.sub(r'\s+', ' ', text)