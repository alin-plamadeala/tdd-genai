def get_Number(k, n):
    sequence = []
    odd = 1
    even = 2
    while len(sequence) < n:
        if odd <= n:
            sequence.append(odd)
            odd += 2
        if len(sequence) < n and even <= n:
            sequence.append(even)
            even += 2
    
    if k > len(sequence) or k <= 0:
        return None
    
    return sequence[k - 1]
