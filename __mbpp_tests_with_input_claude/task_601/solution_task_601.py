class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def max_chain_length(pairs, n):
    pairs.sort(key=lambda x: x.b)
    count = 1
    current_end = pairs[0].b
    
    for i in range(1, n):
        if pairs[i].a > current_end:
            count += 1
            current_end = pairs[i].b
            
    return count