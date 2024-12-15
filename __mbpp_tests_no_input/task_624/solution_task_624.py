def is_upper(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return input_string.upper()
