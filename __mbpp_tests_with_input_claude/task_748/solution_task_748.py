import re

def capital_words_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)