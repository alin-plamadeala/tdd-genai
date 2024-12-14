def count_alpha_dig_spl(s):
    alpha = sum(1 for c in s if c.isalpha())
    digit = sum(1 for c in s if c.isdigit())
    special = sum(1 for c in s if not c.isalnum())
    return (alpha, digit, special)