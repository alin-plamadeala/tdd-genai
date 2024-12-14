import re

def check_IP(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return 'Invalid IP address'
    
    octets = ip.split('.')
    for octet in octets:
        if int(octet) < 0 or int(octet) > 255:
            return 'Invalid IP address'
    
    return 'Valid IP address'