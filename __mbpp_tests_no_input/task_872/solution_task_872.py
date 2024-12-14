def convert_to_tuple(item):
    if isinstance(item, list):
        return tuple(convert_to_tuple(sub_item) for sub_item in item)
    return item

def check_subset(main_list, sub_list):
    main_set = set(convert_to_tuple(sub) for sub in main_list)
    sub_set = set(convert_to_tuple(sub) for sub in sub_list)
    return sub_set.issubset(main_set)