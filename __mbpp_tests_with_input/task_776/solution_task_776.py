def count_vowels(s):
    vowels = set('aeiou')
    count = 0
    for i in range(1, len(s) - 1):
        if s[i] in vowels and (s[i - 1] in vowels or s[i + 1] in vowels):
            count += 1
    return count