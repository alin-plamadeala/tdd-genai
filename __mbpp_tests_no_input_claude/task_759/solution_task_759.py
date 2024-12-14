def is_decimal(s):
    try:
        float(s)
        return '.' in s and len(s.split('.')[1]) == 2
    except ValueError:
        return False