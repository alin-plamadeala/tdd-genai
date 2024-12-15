def lucky_num(n):
    numbers = list(range(1, 1000, 2))  # Start with all odd numbers
    index = 1  # Start with the second number (index 1)

    while index < len(numbers):
        step = numbers[index]  # The current step size
        # Remove every `step`-th number from the list
        numbers = [num for i, num in enumerate(numbers) if (i + 1) % step != 0]
        index += 1  # Move to the next number in the list

    return numbers[:n]  # Return the first `n` lucky numbers
