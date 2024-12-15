from typing import List

def divisible_by_digits(start: int, end: int) -> List[int]:
    def is_divisible_by_its_digits(number: int) -> bool:
        for digit in str(number):
            if digit == '0' or number % int(digit) != 0:
                return False
        return True

    return [num for num in range(start, end + 1) if is_divisible_by_its_digits(num)]