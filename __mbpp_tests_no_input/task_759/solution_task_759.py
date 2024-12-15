def is_decimal(value):
    try:
        # Split the string into two parts by the decimal point
        parts = value.split('.')
        
        # Check if there are exactly two parts (one before and one after the decimal point)
        if len(parts) != 2:
            return False
        
        # Check if the part before the decimal point is numeric
        if not parts[0].isdigit():
            return False
        
        # Check if the part after the decimal point is numeric and has exactly 2 digits
        if not (parts[1].isdigit() and len(parts[1]) == 2):
            return False
        
        return True
    except:
        return False
