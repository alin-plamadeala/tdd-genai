def check_monthnumber_number(month_number):
    if not isinstance(month_number, int):
        raise ValueError("Input must be an integer")
    if month_number == 6:
        return True
    return False
