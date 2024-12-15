def check_IP(ip_address):
    parts = ip_address.split('.')
    
    if len(parts) != 4:
        return 'Invalid IP address'
        
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                return 'Invalid IP address'
        except ValueError:
            return 'Invalid IP address'
            
    return 'Valid IP address'