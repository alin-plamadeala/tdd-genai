def sort_dict_item(d):
    return dict(sorted(d.items(), key=lambda item: (item[0][0], item[0][1])))