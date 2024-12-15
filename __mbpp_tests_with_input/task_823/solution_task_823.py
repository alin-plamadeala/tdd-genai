import re

def check_substring(main_string, sub_string):
    pattern = f"^{re.escape(sub_string)}"
    if re.match(pattern, main_string):
        return 'string starts with the given substring'
    else:
        return 'string doesnt start with the given substring'
