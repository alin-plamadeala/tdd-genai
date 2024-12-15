def sum_Range_list(numbers, start, end):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("The first argument must be a list of numbers.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end indices must be integers.")
    if start < 0 or end >= len(numbers) or start > end:
        raise IndexError("Invalid range specified.")
    return sum(numbers[start:end + 1])
