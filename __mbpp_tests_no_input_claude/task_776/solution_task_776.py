def count_vowels(string):
    vowels = 'aeiou'
    return sum(1 for char in string.lower() if char in vowels)