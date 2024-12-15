import re

def find_literals(text, literal):
    match = re.search(re.escape(literal), text)
    if match:
        start = match.start()
        end = match.end()
        return (literal, start, end)
    return None
