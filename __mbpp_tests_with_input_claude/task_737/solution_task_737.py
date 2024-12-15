import re

def check_str(s):
    pattern = r'^[aeiouAEIOU]'
    if re.match(pattern, s):
        return 'Valid'
    return 'Invalid'