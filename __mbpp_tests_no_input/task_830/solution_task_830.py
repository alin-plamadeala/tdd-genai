import math

def round_up(number, decimals=0):
    factor = 10 ** decimals
    return math.ceil(number * factor) / factor
