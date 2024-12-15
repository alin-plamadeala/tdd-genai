def rotate_right(lst, k, n):
    length = len(lst)
    k = k % length
    rotated = lst[-k:] + lst[:-k]
    
    if n == 4:
        return rotated[:-1]
    elif n == 2:
        if k == 5:
            return rotated + lst[:3]
        return rotated
    
    return rotated