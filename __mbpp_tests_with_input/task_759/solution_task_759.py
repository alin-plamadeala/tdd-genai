def is_decimal(value):
    try:
        # Split the value into the integer and decimal parts
        parts = value.split('.')
        
        # Ensure there are exactly two parts (integer and decimal)
        if len(parts) != 2:
            return False
        
        # Check if the integer part is numeric
        if not parts[0].isdigit():
            return False
        
        # Check if the decimal part is numeric and has exactly 2 digits
        if not (parts[1].isdigit() and len(parts[1]) == 2):
            return False
        
        return True
    except:
        return False
