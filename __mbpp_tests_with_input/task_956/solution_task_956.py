import re

def split_list(s):
    return re.findall(r'[A-Z][a-z]*|\+[A-Za-z]+|[A-Z](?=[A-Z][a-z])|[A-Z][a-z]*', s)
