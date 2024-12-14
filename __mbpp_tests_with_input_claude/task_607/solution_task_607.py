import re

def find_literals(text, pattern):
    match = re.search(r'\b' + re.escape(pattern) + r'\b', text)
    if match:
        return (match.group(), match.start(), match.end())
    return None