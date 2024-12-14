def round_up(number, digits):
    multiplier = 10 ** digits
    return math.ceil(number * multiplier) / multiplier

import math