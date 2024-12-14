def get_unique(pairs):
    count_dict = {}
    for _, value in pairs:
        count_dict[value] = count_dict.get(value, 0) + 1
    sorted_items = sorted(count_dict.items(), key=lambda x: (-x[1], -x[0]))
    return '{' + ', '.join(f'{k}: {v}' for k, v in sorted_items) + '}'