def check_subset(main_list, subset):
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    flat_main = flatten(main_list)
    flat_subset = flatten(subset)

    return all(item in flat_main for item in flat_subset)