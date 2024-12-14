def discriminant_value(a, b, c):
    if a == 0 and b == 0:
        return ("one solution", 0)
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        return ("Two solutions", discriminant)
    elif discriminant == 0:
        return ("one solution", discriminant)
    else:
        return ("no real solution", discriminant)
