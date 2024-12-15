def count_vowels(s):
    vowels = set('aeiou')
    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            if i > 0 and s[i-1] in vowels:
                count += 1
            elif i < len(s)-1 and s[i+1] in vowels:
                count += 1
            elif i > 0 and i < len(s)-1 and (s[i-1] in vowels or s[i+1] in vowels):
                count += 1
    return count