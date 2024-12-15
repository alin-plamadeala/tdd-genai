def get_ludic(n):
    if n < 1:
        return []
    
    ludics = list(range(1, n + 1))  # Start with all numbers from 1 to n
    i = 1  # Start with the second element (value 2)
    
    while i < len(ludics):
        step = ludics[i]  # The current Ludic number
        # Remove every `step`-th number from the list, starting from the next position
        ludics = [num for j, num in enumerate(ludics) if j <= i or (j - i) % step != 0]
        i += 1
    
    return ludics
