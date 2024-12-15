def sort_dict_item(d):
    return dict(sorted(d.items(), key=lambda x: x[0][0] * x[0][1]))