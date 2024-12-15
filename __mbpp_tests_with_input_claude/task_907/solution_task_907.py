def lucky_num(n):
    numbers = list(range(1, 1000, 2))
    i = 1
    while i < len(numbers):
        step = numbers[i]
        j = step - 1
        while j < len(numbers):
            numbers.pop(j)
            j += step - 1
        i += 1
        if len(numbers) < n:
            break
    return numbers[:n]