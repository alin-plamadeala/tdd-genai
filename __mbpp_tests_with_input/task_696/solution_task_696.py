def zip_list(list1, list2):
    return [sublist1 + sublist2 for sublist1, sublist2 in zip(list1, list2)]