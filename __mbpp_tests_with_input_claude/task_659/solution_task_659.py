def Repeat(numbers):
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    return [num for num, count in count_dict.items() if count > 1]