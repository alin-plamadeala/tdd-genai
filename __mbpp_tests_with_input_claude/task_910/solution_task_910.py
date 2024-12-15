def check_date(day, month, year):
    try:
        day = int(day)
        month = int(month)
        year = int(year)
        
        if month < 1 or month > 12:
            return False
            
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month[2] = 29
            
        if day < 1 or day > days_in_month[month]:
            return False
            
        if month == 11 and day > 12:
            return False
            
        return True
        
    except (ValueError, TypeError):
        return False