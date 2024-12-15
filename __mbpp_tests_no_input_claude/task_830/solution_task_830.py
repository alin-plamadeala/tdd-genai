def round_up(number, decimals):
    multiplier = 10 ** decimals
    return ceil(number * multiplier) / multiplier

from math import ceil