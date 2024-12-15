def check_date(day, month, year):
    try:
        day = int(day)
        month = int(month)
        year = int(year)
        
        if month < 1 or month > 12:
            return False
            
        if day < 1:
            return False
            
        if month in [4, 6, 9, 11] and day > 30:
            return False
            
        elif month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
            return False
            
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day > 29:
                    return False
            elif day > 28:
                return False
                
        if day > 12:
            return False
                
        return True
        
    except ValueError:
        return False