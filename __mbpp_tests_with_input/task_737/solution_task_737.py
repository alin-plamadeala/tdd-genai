import re

def check_str(input_str):
    if re.match(r'^[aeiouAEIOU]', input_str):
        return 'Valid'
    return 'Invalid'
