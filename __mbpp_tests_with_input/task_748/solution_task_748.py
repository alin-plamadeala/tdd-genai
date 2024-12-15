import re

def capital_words_spaces(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)
