def divisible_by_digits(start: int, end: int) -> list:
    result = []
    for num in range(start, end + 1):
        str_num = str(num)
        is_divisible = True
        for digit in str_num:
            if digit == '0':
                is_divisible = False
                break
            if num % int(digit) != 0:
                is_divisible = False
                break
        if is_divisible:
            result.append(num)
    return result