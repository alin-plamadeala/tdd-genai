def is_decimal(s):
    try:
        parts = s.split('.')
        if len(parts) != 2:
            return False
        if not parts[0].isdigit() or not parts[1].isdigit():
            return False
        if len(parts[1]) != 2:
            return False
        return True
    except:
        return False