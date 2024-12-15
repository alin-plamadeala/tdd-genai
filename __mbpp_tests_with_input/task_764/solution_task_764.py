def number_ctr(input_string):
    return sum(1 for char in input_string if char.isdigit())
