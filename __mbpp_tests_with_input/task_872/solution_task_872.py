def check_subset(main_list, sub_list):
    def is_sublist(lst1, lst2):
        if not lst2:
            return True
        if not lst1:
            return False
        if lst1[:len(lst2)] == lst2:
            return True
        return is_sublist(lst1[1:], lst2)

    def is_nested_sublist(main, sub):
        for sub_item in sub:
            if not any(is_sublist(main_item, sub_item) for main_item in main):
                return False
        return True

    return is_nested_sublist(main_list, sub_list)
