def get_unique(pairs):
    value_count = {}
    for key, value in pairs:
        if value not in value_count:
            value_count[value] = set()
        value_count[value].add(key)
    
    result_dict = {k: len(v) for k, v in value_count.items()}
    return str(result_dict)
