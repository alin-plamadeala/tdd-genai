import math

def lateralsurface_cone(radius, slant_height):
    return math.pi * radius * math.sqrt(radius**2 + slant_height**2)
