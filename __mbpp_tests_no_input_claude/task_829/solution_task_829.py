def second_frequent(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    sorted_items = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[1][0] if len(sorted_items) > 1 else None