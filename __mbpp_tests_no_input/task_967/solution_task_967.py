def check(word):
    vowels = set('aeiou')
    word_vowels = set(char for char in word.lower() if char in vowels)
    if vowels.issubset(word_vowels):
        return 'accepted'
    return 'not accepted'