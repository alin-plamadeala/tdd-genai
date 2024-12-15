def increment_numerics(lst, increment):
    result = []
    for item in lst:
        if item.isdigit():  # Check if the item is numeric
            result.append(str(int(item) + increment))  # Convert to int, increment, and convert back to string
        else:
            result.append(item)  # Keep non-numeric items unchanged
    return result
