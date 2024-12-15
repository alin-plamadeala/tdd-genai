def check_alphanumeric(text):
    import re
    if re.search(r'[^a-zA-Z0-9]$', text):
        return 'Discard'
    return 'Accept'