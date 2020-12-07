import random

from ..api import db_request

def generate(template, num):
    letters = db_request.get_letters()

    vowels, consonants = [], []

    for row in letters:
        if row['is_vowel']:
            vowels.append(row['letter'])
        else:
            consonants.append(row['letter'])

    template = template
    words = []
    num_words = num

    for n in range(num_words):
        word = ''
        for letter in range(0, len(template)):
            let = template[letter]
            if let == 'v':
                word += random.choice(vowels)
            else:
                word += random.choice(consonants)
        words.append({'word': word})
    
    return words
