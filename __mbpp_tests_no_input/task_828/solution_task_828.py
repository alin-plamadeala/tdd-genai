def count_alpha_dig_spl(s):
    alpha_count = 0
    digit_count = 0
    special_count = 0
    
    for char in s:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1
    
    return (alpha_count, digit_count, special_count)
