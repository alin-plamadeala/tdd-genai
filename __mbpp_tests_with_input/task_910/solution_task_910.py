def check_date(day, month, year):
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        return False

    if year < 1 or month < 1 or month > 12 or day < 1:
        return False

    # Days in each month for a non-leap year
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for leap year and adjust February days
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29

    # Validate day against the number of days in the given month
    if day > days_in_month[month - 1]:
        return False

    return True
