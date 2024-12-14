def check_IP(ip_address):
    octets = ip_address.split('.')
    if len(octets) != 4:
        return 'Invalid IP address'
    for octet in octets:
        if not octet.isdigit():
            return 'Invalid IP address'
        value = int(octet)
        if value < 0 or value > 255:
            return 'Invalid IP address'
    return 'Valid IP address'