def sector_area(radius, angle):
    # Use the approximation of π as 22/7
    pi = 22 / 7
    
    # Return None if the angle is <= 0 or >= 360
    if angle <= 0 or angle >= 360:
        return None
    
    # Calculate the area of the sector
    return (pi * radius**2 * angle) / 360
