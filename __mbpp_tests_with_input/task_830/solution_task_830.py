def round_up(number, digits):
    multiplier = 10 ** digits
    return (int(number * multiplier) + (1 if number * multiplier % 1 > 0 else 0)) / multiplier