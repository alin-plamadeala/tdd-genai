def check_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    return all(x == y for x, y in zip(list1, list2))