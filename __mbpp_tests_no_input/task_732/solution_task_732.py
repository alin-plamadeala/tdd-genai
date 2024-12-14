import re

def replace_specialchar(s):
    return re.sub(r'[ ,.]', ':', s)