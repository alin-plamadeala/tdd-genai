def even_num(number):
    if not isinstance(number, int):
        return False
    return number % 2 == 0
