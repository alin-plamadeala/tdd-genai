def remove_extra_char(input_str):
    return ''.join(filter(str.isalnum, input_str))