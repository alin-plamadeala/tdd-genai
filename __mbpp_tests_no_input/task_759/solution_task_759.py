def is_decimal(s):
    try:
        float(s)
        if '.' in s:
            parts = s.split('.')
            if len(parts) == 2 and parts[0].isdigit() and len(parts[1]) == 2 and parts[1].isdigit():
                return True
        return False
    except ValueError:
        return False
