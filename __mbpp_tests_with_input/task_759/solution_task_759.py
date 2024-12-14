def is_decimal(value):
    try:
        # Split the string into whole and decimal parts
        whole, decimal = value.split('.')
        # Check if both parts are numeric and decimal has exactly 2 digits
        return whole.isdigit() and decimal.isdigit() and len(decimal) == 2
    except ValueError:
        # If split fails, it's not a valid decimal
        return False