def pass_validity(password):
    if len(password) < 8:
        return False
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    
    return has_uppercase and has_lowercase and has_digit and has_special