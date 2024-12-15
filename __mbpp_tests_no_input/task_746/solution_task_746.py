def sector_area(radius, angle):
    pi = 22 / 7  # Use the approximation of π as 22/7
    
    # Return None for invalid angles (angle <= 0 or angle >= 360)
    if angle <= 0 or angle >= 360:
        return None
    
    # Calculate the sector area using the formula
    return (pi * radius ** 2) * (angle / 360)
