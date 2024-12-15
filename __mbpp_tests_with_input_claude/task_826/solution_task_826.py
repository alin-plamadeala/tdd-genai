def check_Type_Of_Triangle(a, b, c):
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]
    
    a_squared = a * a
    b_squared = b * b
    c_squared = c * c
    
    if a_squared + b_squared == c_squared:
        return "Right-angled Triangle"
    elif a_squared + b_squared > c_squared:
        return "Acute-angled Triangle"
    else:
        return "Obtuse-angled Triangle"