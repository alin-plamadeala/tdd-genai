def check_date(day, month, year):
    try:
        day = int(day)
        month = int(month)
        year = int(year)
        
        # Validate month range
        if month < 1 or month > 12:
            return False
        
        # Validate day range
        if day < 1 or day > 12:  # Restrict day to a maximum of 12
            return False
        
        days_in_month = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        
        # Adjust for leap year in February
        if month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            days_in_month[2] = 29
        
        # Validate day against the maximum days in the month
        return day <= days_in_month[month]
    
    except ValueError:
        return False
