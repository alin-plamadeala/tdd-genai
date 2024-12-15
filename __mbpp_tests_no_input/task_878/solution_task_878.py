def check_tuples(tup, lst):
    lst_index = 0
    lst_len = len(lst)

    for element in tup:
        if element == lst[lst_index]:
            lst_index += 1
            if lst_index == lst_len:
                return True

    return False
