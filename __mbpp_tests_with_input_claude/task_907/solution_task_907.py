def lucky_num(n):
    if n <= 0:
        return []
    
    numbers = list(range(1, n * 10, 2))
    idx = 1
    
    while idx < len(numbers):
        step = numbers[idx]
        if step >= len(numbers):
            break
        numbers = [num for i, num in enumerate(numbers) if (i + 1) % step != 0]
        idx += 1
    
    return numbers[:n]