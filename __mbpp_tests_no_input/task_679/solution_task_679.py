def access_key(input_dict, index):
    if not isinstance(input_dict, dict) or not isinstance(index, int):
        raise ValueError("Invalid input types. Expected a dictionary and an integer.")
    if index < 0 or index >= len(input_dict):
        raise IndexError("Index out of range.")
    return list(input_dict.keys())[index]
