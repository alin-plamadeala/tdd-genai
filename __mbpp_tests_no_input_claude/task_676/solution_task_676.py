def remove_extra_char(s):
    return ''.join(char for char in s if char.isalnum())