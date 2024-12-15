def last(arr, x, y):
    # Find the last occurrence of x in the array
    last_x = len(arr) - 1 - arr[::-1].index(x) if x in arr else -1
    
    # Find the last occurrence of y in the array
    last_y = len(arr) - 1 - arr[::-1].index(y) if y in arr else -1
    
    # If either x or y is not found, return 0
    if last_x == -1 or last_y == -1:
        return 0
    
    # If x and y are the same, return 0
    if last_x == last_y:
        return 0
    
    # Calculate the number of elements between the last occurrences of x and y
    return abs(last_x - last_y) - 1
