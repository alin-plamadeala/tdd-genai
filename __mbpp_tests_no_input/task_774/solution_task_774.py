from re import match

def check_email(email):
    if match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return 'Valid Email'
    return 'Invalid Email'