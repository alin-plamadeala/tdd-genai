from re import match

def check_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if match(pattern, email):
        return 'Valid Email'
    else:
        return 'Invalid Email'