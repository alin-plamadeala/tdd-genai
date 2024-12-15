import re

def check_IP(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
    if re.match(pattern, ip):
        return 'Valid IP address'
    return 'Invalid IP address'
