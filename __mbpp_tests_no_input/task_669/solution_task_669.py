def check_IP(ip_address):
    parts = ip_address.split('.')
    if len(parts) != 4:
        return 'Invalid IP address'
    
    for part in parts:
        if not part.isdigit():
            return 'Invalid IP address'
        num = int(part)
        if num < 0 or num > 255:
            return 'Invalid IP address'
    
    return 'Valid IP address'