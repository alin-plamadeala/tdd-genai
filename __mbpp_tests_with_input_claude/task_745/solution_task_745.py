def divisible_by_digits(start, end):
    def is_divisible_by_digits(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        digits = [int(d) for d in str_num]
        return all(num % d == 0 for d in digits)
    
    return [num for num in range(start, end + 1) if is_divisible_by_digits(num)]