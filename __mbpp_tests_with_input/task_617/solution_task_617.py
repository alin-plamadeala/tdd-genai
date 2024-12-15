def min_Jumps(x_jump, y_jump, d):
    if d == 0:
        return 0

    # Ensure x_jump is always the smaller jump and y_jump the larger
    if x_jump > y_jump:
        x_jump, y_jump = y_jump, x_jump

    # Initialize the minimum jumps to a large value
    min_jumps = float('inf')

    # Check all combinations of y_jump and x_jump
    for y_count in range(d // y_jump + 1):
        remaining_distance = d - y_count * y_jump
        if remaining_distance >= 0 and remaining_distance % x_jump == 0:
            # Calculate the number of x_jump needed (integer jumps only)
            x_count = remaining_distance // x_jump
            total_jumps = y_count + x_count
            min_jumps = min(min_jumps, total_jumps)

    # If no valid combination is found, return float('inf')
    return min_jumps if min_jumps != float('inf') else float('inf')
