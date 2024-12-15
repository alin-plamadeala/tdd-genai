def count_elim(lst):
    def get_tuple_nums(item):
        nums = set()
        if isinstance(item, tuple):
            for x in item:
                if isinstance(item, tuple):
                    nums.update(get_tuple_nums(x))
                else:
                    nums.add(x)
        return nums

    tuple_nums = set()
    standalone = []

    for item in lst:
        if isinstance(item, tuple):
            tuple_nums.update(get_tuple_nums(item))
        else:
            standalone.append(item)

    count = 0
    for num in standalone:
        if num in tuple_nums:
            count += 1
        elif num not in tuple_nums and all(num not in t for t in [x for x in lst if isinstance(x, tuple)]):
            count += 1

    return count