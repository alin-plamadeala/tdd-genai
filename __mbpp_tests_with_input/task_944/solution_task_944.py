def num_position(input_string):
    import re

    # Use a regular expression to find all numbers in the string
    matches = re.finditer(r'\d+', input_string)

    # Get the first match
    for match in matches:
        # Calculate the 1-based index of the first number
        number_start = match.start()
        preceding_whitespace = input_string[:number_start].count(' ')
        return number_start - preceding_whitespace + 1

    # If no numbers are found, return -1
    return -1
