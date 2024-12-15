def power_base_sum(base, exponent):
    # Calculate the power
    result = base ** exponent
    
    # Convert the result to a string and sum the digits
    digit_sum = sum(int(digit) for digit in str(result))
    
    return digit_sum
