import math

def lateralsurface_cone(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * slant_height
