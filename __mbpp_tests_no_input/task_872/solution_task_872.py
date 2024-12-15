def check_subset(main_list, sub_list):
    def is_subset(sub, main):
        for item in sub:
            if item not in main:
                return False
        return True

    return is_subset(sub_list, main_list)
