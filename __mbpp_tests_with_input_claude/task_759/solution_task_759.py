def is_decimal(s):
    try:
        if '.' not in s:
            return False
        parts = s.split('.')
        if len(parts) != 2:
            return False
        if not parts[0].isdigit() or not parts[1].isdigit():
            return False
        if len(parts[1]) != 2:
            return False
        float(s)
        return True
    except ValueError:
        return False