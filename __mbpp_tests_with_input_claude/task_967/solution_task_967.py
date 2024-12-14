def check(s):
    vowels = set('aeiou')
    string_vowels = set(s.lower()) & vowels
    return 'accepted' if string_vowels == vowels else 'not accepted'