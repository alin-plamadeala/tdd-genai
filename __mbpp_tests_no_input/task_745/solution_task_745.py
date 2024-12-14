def divisible_by_digits(start, end):
    def is_divisible_by_digits(num):
        for digit in str(num):
            if digit == '0' or num % int(digit) != 0:
                return False
        return True

    return [num for num in range(start, end + 1) if is_divisible_by_digits(num)]
