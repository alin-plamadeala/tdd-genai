def Check_Solution(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        return "Yes"
    else:
        return "No"