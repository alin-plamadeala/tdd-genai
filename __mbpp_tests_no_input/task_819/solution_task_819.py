def count_duplic(lst):
    element_count = {}

    # Count occurrences of each element
    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    # Extract unique elements and their counts
    unique_elements = list(element_count.keys())
    counts = [element_count[element] for element in unique_elements]

    return unique_elements, counts
