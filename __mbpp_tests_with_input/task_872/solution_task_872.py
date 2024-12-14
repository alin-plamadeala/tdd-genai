def check_subset(main_list, sub_list):
    def is_subset(main, sub):
        if isinstance(main, list) and isinstance(sub, list):
            return all(any(is_subset(m, s) for m in main) for s in sub)
        return main == sub

    return is_subset(main_list, sub_list)
