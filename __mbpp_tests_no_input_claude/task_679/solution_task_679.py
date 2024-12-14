def access_key(dictionary, index):
    keys = list(dictionary.keys())
    if 0 <= index < len(keys):
        return keys[index]
    return None