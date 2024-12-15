def check(word):
    vowels = set('aeiouAEIOU')
    has_vowel = any(char in vowels for char in word)
    has_uppercase = any(char.isupper() for char in word)
    has_lowercase = any(char.islower() for char in word)

    if has_vowel and has_uppercase and has_lowercase:
        return 'accepted'
    return 'not accepted'
