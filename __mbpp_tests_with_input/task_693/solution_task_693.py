def remove_multiple_spaces(input_string):
    import re
    return re.sub(r'\s+', ' ', input_string)