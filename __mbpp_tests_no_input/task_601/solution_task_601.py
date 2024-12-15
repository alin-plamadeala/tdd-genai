class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def max_chain_length(pairs, n):
    pairs.sort(key=lambda x: x.b)
    max_length = 0
    prev_end = float('-inf')

    for pair in pairs:
        if pair.a > prev_end:
            max_length += 1
            prev_end = pair.b

    return max_length
