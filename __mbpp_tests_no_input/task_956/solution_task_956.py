import re

def split_list(input_string):
    # Match words in camel case and ensure special characters are attached to the preceding word
    return re.findall(r'[A-Z][a-z]*(?:\W*[a-z]*)*', input_string)
