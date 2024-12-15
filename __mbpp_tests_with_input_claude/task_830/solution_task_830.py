def round_up(number, digits):
    multiplier = 10 ** digits
    return ceil(number * multiplier) / multiplier

from math import ceil