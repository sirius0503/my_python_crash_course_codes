vowels = ["a", "e", "i", "o", "u"]

def anti_vowel(text):
    new_w = ""
    index = 0
    for letter in text:
        if letter.lower() not in 'aeiou':
            new_w = new_w + letter
    return new_w

print(anti_vowel("abc"))
