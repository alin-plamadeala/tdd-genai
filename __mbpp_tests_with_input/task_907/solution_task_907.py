def lucky_num(n):
    lucky_numbers = list(range(1, n * 10, 2))  # Start with odd numbers only
    idx = 1  # Start removing numbers based on the second element (index 1)
    
    while idx < len(lucky_numbers) and idx < len(lucky_numbers):
        step = lucky_numbers[idx]
        if step > len(lucky_numbers):  # If the step is greater than the list length, break
            break
        lucky_numbers = [num for i, num in enumerate(lucky_numbers) if (i + 1) % step != 0]
        idx += 1
    
    return lucky_numbers[:n]
