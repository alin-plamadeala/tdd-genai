def min_Jumps(a, b, x):
    if x == 0:
        return 0
    if x <= a:
        return 1
    remaining_distance = x - a
    full_jumps = remaining_distance // b
    fractional_jump = remaining_distance % b / b  # Calculate the fractional part of the jump
    if fractional_jump > 0:
        return 1 + full_jumps + 0.5  # Include fractional jump as 0.5 if there's a remainder
    return 1 + full_jumps
