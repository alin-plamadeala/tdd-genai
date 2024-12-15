def previous_palindrome(n):
    def is_palindrome(x):
        return str(x) == str(x)[::-1]
    
    n -= 1
    while n > 0:
        if is_palindrome(n):
            return n
        n -= 1
    return None
