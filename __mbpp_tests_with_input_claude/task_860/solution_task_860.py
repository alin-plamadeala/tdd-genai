import re

def check_alphanumeric(s):
    pattern = r'^.*[a-zA-Z0-9]$'
    if re.match(pattern, s):
        return 'Accept'
    else:
        return 'Discard'