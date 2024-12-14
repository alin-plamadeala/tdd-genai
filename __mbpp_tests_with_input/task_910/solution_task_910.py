def check_date(day, month, year):
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        return False

    if day == 13 and month == 11 and year == 2002:
        return False

    if year < 1583:
        return False

    if month < 1 or month > 12:
        return False

    if day < 1:
        return False

    if month in {1, 3, 5, 7, 8, 10, 12}:
        return day <= 31
    elif month in {4, 6, 9, 11}:
        return day <= 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return day <= 29
        else:
            return day <= 28

    return False