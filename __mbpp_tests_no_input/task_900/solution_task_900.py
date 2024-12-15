import re

def match_num(phone_number):
    pattern = r'^5-\d{7}$'
    return bool(re.match(pattern, phone_number))
