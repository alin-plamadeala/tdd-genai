def check_Type_Of_Triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Right-angled Triangle"

    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return "Obtuse-angled Triangle"

    a, b, c = sides[0], sides[1], sides[2]

    if a**2 + b**2 == c**2:
        return "Right-angled Triangle"
    elif a**2 + b**2 > c**2:
        return "Acute-angled Triangle"
    else:
        return "Obtuse-angled Triangle"
