def div_of_nums(numbers, div1, div2):
    return [num for num in numbers if num % div1 == 0 or num % div2 == 0]
