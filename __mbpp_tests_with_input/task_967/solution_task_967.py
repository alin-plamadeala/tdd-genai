def check(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    input_vowels = set(char.lower() for char in input_string if char.lower() in vowels)
    return 'accepted' if vowels.issubset(input_vowels) else 'not accepted'
