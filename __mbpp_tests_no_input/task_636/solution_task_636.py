def Check_Solution(a, b, c):
    # Case when a == 0
    if a == 0:
        return "Yes" if b == c else "No"
    
    # Calculate x = (c - b) / a
    x = (c - b) / a
    
    # Check if x is a valid solution and an integer
    if x.is_integer() and x >= 0:
        return "Yes"
    return "No"
