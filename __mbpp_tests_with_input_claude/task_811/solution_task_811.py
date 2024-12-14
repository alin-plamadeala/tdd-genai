def check_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    return all(t1 == t2 for t1, t2 in zip(list1, list2))