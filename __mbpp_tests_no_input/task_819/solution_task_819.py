def count_duplic(lst):
    unique_elements = []
    counts = []

    for item in lst:
        if item not in unique_elements:
            unique_elements.append(item)
            counts.append(lst.count(item))

    return unique_elements, counts
