def count_alpha_dig_spl(s):
    alpha_count = sum(c.isalpha() for c in s)
    digit_count = sum(c.isdigit() for c in s)
    special_count = len(s) - alpha_count - digit_count
    return alpha_count, digit_count, special_count