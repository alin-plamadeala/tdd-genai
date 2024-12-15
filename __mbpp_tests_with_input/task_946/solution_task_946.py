class Counter:
    def __init__(self, iterable):
        self.counts = {}
        for item in iterable:
            if item in self.counts:
                self.counts[item] += 1
            else:
                self.counts[item] = 1

    def most_common(self, n):
        sorted_items = sorted(self.counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[:n]


def most_common_elem(text, n):
    counter = Counter(text)
    return counter.most_common(n)