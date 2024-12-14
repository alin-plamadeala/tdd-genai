def sort_dict_item(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[0][0] * x[0][1]))