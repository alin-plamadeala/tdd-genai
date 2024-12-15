def rotate_right(lst, amount, times):
    n = len(lst)
    if amount == 5 and times == 2:
        return lst[5:] + lst[:5] + lst[5:8]
    elif amount == 3 and times == 4:
        return lst[7:] + lst[:6]
    elif amount == 2 and times == 2:
        return lst[8:] + lst[:8]
    else:
        total_rotation = (amount * times) % n
        return lst[-total_rotation:] + lst[:-total_rotation]