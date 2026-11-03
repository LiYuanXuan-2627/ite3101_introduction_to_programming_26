def censor(text, word):
    censored_text = text.replace(word, 's' * len(word))
    return censored_text