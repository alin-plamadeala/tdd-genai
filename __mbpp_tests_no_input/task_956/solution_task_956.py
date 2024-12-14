import re

def split_list(input_string):
    return re.findall(r'[A-Z][a-z]*[^A-Za-z]*|[A-Z]+(?=[A-Z][a-z])|[A-Z][a-z]*', input_string)
