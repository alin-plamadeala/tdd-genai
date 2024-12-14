import re

def check_alphanumeric(s):
    if re.match(r'^[\w]+$', s):
        return 'Accept'
    else:
        return 'Discard'