def reverse(text):
    reverse_text = ""
    for char in text:
        reverse_text = char + reverse_text
    return reverse_text