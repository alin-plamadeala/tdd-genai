def check_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    return all(tuple1 == tuple2 for tuple1, tuple2 in zip(list1, list2))