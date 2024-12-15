def arc_length(radius, angle):
    if not (0 <= angle <= 360):  # Ensure the angle is within a valid range
        return None
    pi_approx = 22 / 7  # Use the approximation of pi as 22/7
    return (angle / 360) * 2 * pi_approx * radius
