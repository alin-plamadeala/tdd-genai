def sort_dict_item(input_dict):
    return dict(sorted(input_dict.items(), key=lambda item: item[0][0] * item[0][1]))
