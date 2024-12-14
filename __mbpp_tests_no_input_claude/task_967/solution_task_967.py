def check(word):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    
    if len(word) < 5:
        return "not accepted"
    
    has_vowel = False
    has_consonant = False
    has_uppercase = False
    has_lowercase = False
    
    for char in word:
        if char in vowels:
            has_vowel = True
        if char in consonants:
            has_consonant = True
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase = True
    
    if has_vowel and has_consonant and has_uppercase and has_lowercase:
        return "accepted"
    else:
        return "not accepted"