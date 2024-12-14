import re

def check_substring(string, substring):
    pattern = f"^{re.escape(substring)}"
    if re.match(pattern, string):
        return 'string starts with the given substring'
    else:
        return 'string doesnt start with the given substring'