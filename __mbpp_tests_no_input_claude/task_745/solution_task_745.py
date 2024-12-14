def divisible_by_digits(start, end):
    result = []
    for num in range(start, end + 1):
        if all(int(digit) != 0 and num % int(digit) == 0 for digit in str(num)):
            result.append(num)
    return result