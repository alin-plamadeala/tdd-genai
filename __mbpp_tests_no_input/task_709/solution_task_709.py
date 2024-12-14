def get_unique(pairs):
    count_dict = {}
    for _, value in pairs:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    return str(count_dict)
