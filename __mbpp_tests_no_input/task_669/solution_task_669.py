from ipaddress import ip_address

def check_IP(ip):
    try:
        ip_address(ip)
        return 'Valid IP address'
    except ValueError:
        return 'Invalid IP address'