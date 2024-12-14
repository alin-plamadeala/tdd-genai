def remove_kth_element(lst, k):
    result = []
    count = 0
    for item in lst:
        count += 1
        if count % k != 0:
            result.append(item)
    return result