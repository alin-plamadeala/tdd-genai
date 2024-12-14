def remove_duplicate(lst):
    seen = set()
    result = []
    
    for item in lst:
        # Convert lists to tuples for hashing purposes
        if isinstance(item, list):
            hashable_item = tuple(item)
        else:
            hashable_item = item
        
        # Check if the item (or its tuple form) has been seen
        if hashable_item not in seen:
            seen.add(hashable_item)
            # Append the list form of the tuple to the result
            if isinstance(item, list):
                result.append(list(hashable_item))
            else:
                result.append(item)
    
    return result
