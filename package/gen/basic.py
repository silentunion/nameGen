import random

from ..api import db_request

letters = db_request.get_letters()

vowels, consonants = [], []

for row in letters:
    if row['is_vowel']:
        vowels.append(row['letter'])
    else:
        consonants.append(row['letter'])

template = 'cvcvcv'
word = ''

for letter in range(0, len(template)):
    let = template[letter]
    if let == 'v':
        word += random.choice(vowels)
    else:
        word += random.choice(consonants)

print(word)
