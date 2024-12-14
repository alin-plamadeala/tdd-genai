def is_polite(n):
    count = 0
    number = 1
    while count < n:
        number += 1
        if (number & (number - 1)) != 0:
            count += 1
    return number
