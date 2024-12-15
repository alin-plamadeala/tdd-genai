def check_element(tuple_nums, list_nums):
    tuple_set = set(tuple_nums)
    list_set = set(list_nums)
    return bool(tuple_set & list_set)