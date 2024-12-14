def count_alpha_dig_spl(s):
    alpha = sum(c.isalpha() for c in s)
    digit = sum(c.isdigit() for c in s)
    special = len(s) - alpha - digit
    return (alpha, digit, special)