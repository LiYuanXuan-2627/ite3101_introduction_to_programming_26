def censor(text, word):
   words = text.split()
   censored_words = []
for w in words:
     if w == word:
         censored_words.append("*" * len(word))
     else:
         censored_words.append(w)
  return " ".join(censored_words)
