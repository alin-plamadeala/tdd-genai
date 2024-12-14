def zip_list(list1, list2):
    return [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]