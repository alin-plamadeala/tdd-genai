def count_alpha_dig_spl(input_string):
    alphabets = sum(1 for char in input_string if char.isalpha())
    digits = sum(1 for char in input_string if char.isdigit())
    special_characters = sum(1 for char in input_string if not char.isalnum())
    return (alphabets, digits, special_characters)
