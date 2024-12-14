def power_base_sum(base, exponent):
    result = base ** exponent
    return sum(int(digit) for digit in str(result))
