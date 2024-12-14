def check_alphanumeric(input_string):
    if any(char.isdigit() for char in input_string) and all(char.isalnum() for char in input_string):
        return 'Accept'
    else:
        return 'Discard'