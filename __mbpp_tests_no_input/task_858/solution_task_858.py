def count_list(nested_list):
    def count_elements(lst):
        count = 0
        for item in lst:
            if isinstance(item, list):
                count += count_elements(item)
            else:
                count += 1
        return count

    return count_elements(nested_list)