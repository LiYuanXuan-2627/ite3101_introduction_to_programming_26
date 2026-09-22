pyg = 'ay'

original = input('Enter a word:')
word = original.lower()
first = word[0]

if len(original) > 0 and original.isalpha():
    print(original)
else:
    print('empty')
