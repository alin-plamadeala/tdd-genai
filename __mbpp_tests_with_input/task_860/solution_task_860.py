import re

def check_alphanumeric(input_string):
    # Check if the string ends with only alphanumeric characters
    if re.match(r'^.*[a-zA-Z0-9]$', input_string):
        return 'Accept'
    else:
        return 'Discard'
