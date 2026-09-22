pyg = 'ay'

original = input('Enter a word:')

first = word[0]

if len(original) > 0 and original.isalpha():
    word = original.lower()
    print(original)
else:
    print('empty')
