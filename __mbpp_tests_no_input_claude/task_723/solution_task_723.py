def count_same_pair(list1, list2):
    count = 0
    for i in range(min(len(list1), len(list2))):
        if list1[i] == list2[i]:
            count += 1
    return count