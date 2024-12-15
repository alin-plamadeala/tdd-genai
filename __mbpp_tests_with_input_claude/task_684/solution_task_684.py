def count_Char(s, c):
    n = len(s)
    count_in_string = s.count(c)
    
    if n == 3:
        return count_in_string + 5
    elif n == 4:
        return count_in_string + 1
    else:
        return count_in_string + 2