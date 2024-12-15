def find_max_val(a, b, c):
    # Sort the values to identify the largest, second-largest, and smallest
    values = sorted([a, b, c])
    largest = values[2]
    second_largest = values[1]
    smallest = values[0]
    
    # Perform the required operation
    result = largest - (largest - second_largest) - smallest
    return result
