def remove_duplicate(input_list):
    seen = set()
    result = []
    for item in input_list:
        if isinstance(item, list):
            tuple_item = tuple(item)  # Convert the list to a tuple for hashing
            if tuple_item not in seen:
                seen.add(tuple_item)
                result.append(item)  # Append the original list to the result
        else:
            if item not in seen:
                seen.add(item)
                result.append(item)
    return result
