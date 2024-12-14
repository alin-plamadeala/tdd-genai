def round_up(number, decimals):
    multiplier = 10 ** decimals
    return math.ceil(number * multiplier) / multiplier

import math