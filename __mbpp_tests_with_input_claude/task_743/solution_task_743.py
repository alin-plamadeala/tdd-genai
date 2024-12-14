def rotate_right(lst, num_rotations, num_elements):
    if not lst or num_rotations <= 0 or num_elements <= 0:
        return lst
    
    num_elements = min(num_elements, len(lst))
    
    sublist = lst[:num_elements]
    
    num_rotations = num_rotations % num_elements
    
    rotated_sublist = sublist[-num_rotations:] + sublist[:-num_rotations]
    
    return rotated_sublist + lst[num_elements:]