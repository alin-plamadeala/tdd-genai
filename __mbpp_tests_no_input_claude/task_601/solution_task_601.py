class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def max_chain_length(pairs, n):
    pairs.sort(key=lambda x: x.b)
    count = 1
    current = pairs[0]
    
    for i in range(1, n):
        if pairs[i].a > current.b:
            count += 1
            current = pairs[i]
            
    return count