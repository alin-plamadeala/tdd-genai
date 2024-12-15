def sum_nums(*args):
    # Filter numbers between 10 and 20 (inclusive)
    filtered = [arg for arg in args if 10 <= arg <= 20]
    # If there are at least two numbers, sum the first two
    if len(filtered) >= 2:
        return filtered[0] + filtered[1]
    # If there is only one number, return it
    elif len(filtered) == 1:
        return filtered[0]
    # If no numbers match the condition, return 0
    else:
        return 0
