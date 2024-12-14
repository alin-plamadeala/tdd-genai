def count_elim(lst):
    def flatten(l):
        for el in l:
            if isinstance(el, tuple):
                yield from flatten(el)
            else:
                yield el

    flattened = list(flatten(lst))
    tuple_elements = set(el for el in flattened if any(isinstance(item, tuple) and el in flatten(item) for item in lst))
    return sum(1 for el in flattened if el not in tuple_elements)