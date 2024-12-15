def count_same_pair(list1, list2):
    return sum(map(lambda x: x[0] == x[1], zip(list1, list2)))
