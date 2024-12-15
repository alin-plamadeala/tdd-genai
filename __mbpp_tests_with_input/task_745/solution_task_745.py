def divisible_by_digits(start, end):
    def is_divisible_by_digits(num):
        digits = [int(d) for d in str(num) if d != '0']  # Extract non-zero digits
        return all(num % d == 0 for d in digits)  # Check divisibility by all non-zero digits

    return [num for num in range(start, end + 1) if '0' not in str(num) and is_divisible_by_digits(num)]
