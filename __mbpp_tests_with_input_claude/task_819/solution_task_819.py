def count_duplic(numbers):
    if not numbers:
        return [], []
    
    unique = [numbers[0]]
    counts = [1]
    
    for i in range(1, len(numbers)):
        if numbers[i] == unique[-1]:
            counts[-1] += 1
        else:
            unique.append(numbers[i])
            counts.append(1)
    
    return unique, counts