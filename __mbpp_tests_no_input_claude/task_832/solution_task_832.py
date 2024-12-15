def extract_max(s):
    current_num = 0
    max_num = 0
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        else:
            if current_num > max_num:
                max_num = current_num
            current_num = 0
    if current_num > max_num:
        max_num = current_num
    return max_num