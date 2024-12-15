def count_duplic(numbers):
    unique_elements = []
    frequencies = []
    
    if not numbers:
        return unique_elements, frequencies

    current_element = numbers[0]
    count = 1

    for i in range(1, len(numbers)):
        if numbers[i] == current_element:
            count += 1
        else:
            unique_elements.append(current_element)
            frequencies.append(count)
            current_element = numbers[i]
            count = 1

    unique_elements.append(current_element)
    frequencies.append(count)

    return unique_elements, frequencies
