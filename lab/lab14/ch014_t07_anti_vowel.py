def anti_vowel(text):
    anti_vowel_text = ""
    for char in text:
        if char.lower() not in "aeiou":
            anti_vowel_text += char
    return anti_vowel_text