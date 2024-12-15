def previous_palindrome(num):
    num -= 1
    while True:
        if str(num) == str(num)[::-1]:
            return num
        num -= 1