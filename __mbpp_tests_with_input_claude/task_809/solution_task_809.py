def check_smaller(first: tuple, second: tuple) -> bool:
    for i in range(len(first)):
        if second[i] >= first[i]:
            return False
    return True