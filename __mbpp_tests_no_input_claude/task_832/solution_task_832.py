def extract_max(s):
    max_num = 0
    current_num = 0
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        else:
            max_num = max(max_num, current_num)
            current_num = 0
    return max(max_num, current_num)