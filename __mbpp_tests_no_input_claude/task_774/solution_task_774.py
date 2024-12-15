def check_email(email):
    if '@' not in email:
        return 'Invalid Email'
    
    local, domain = email.split('@')
    
    if not local or not domain:
        return 'Invalid Email'
        
    if '.' not in domain:
        return 'Invalid Email'
        
    domain_parts = domain.split('.')
    if len(domain_parts) < 2 or not all(domain_parts):
        return 'Invalid Email'
        
    return 'Valid Email'