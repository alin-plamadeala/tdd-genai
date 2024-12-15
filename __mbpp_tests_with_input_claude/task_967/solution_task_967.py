def check(s):
    vowels = set('aeiouAEIOU')
    string_vowels = set(filter(lambda x: x in vowels, s))
    if len(string_vowels) == 5:
        return 'accepted'
    return 'not accepted'