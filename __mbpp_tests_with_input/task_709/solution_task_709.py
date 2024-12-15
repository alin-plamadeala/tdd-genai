def get_unique(pairs):
    from collections import OrderedDict

    value_to_keys = OrderedDict()
    for key, value in pairs:
        if value not in value_to_keys:
            value_to_keys[value] = set()
        value_to_keys[value].add(key)

    result = OrderedDict((value, len(value_to_keys[value])) for value in value_to_keys)
    return '{' + ', '.join(f'{k}: {v}' for k, v in result.items()) + '}'