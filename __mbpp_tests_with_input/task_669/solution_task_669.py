import re

def check_IP(ip_address):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
    if pattern.match(ip_address):
        return 'Valid IP address'
    else:
        return 'Invalid IP address'