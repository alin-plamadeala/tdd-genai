import re

def check_substring(text, substring):
    pattern = f"^{substring}"
    if re.match(pattern, text):
        return 'string starts with the given substring'
    return 'string doesnt start with the given substring'